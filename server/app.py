from flask import Flask, request, make_response
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
from models import db, Employee, Job, Availability

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduler.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
CORS(app)

api = Api(app)
ma = Marshmallow(app)

class JobSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Job

    id = ma.auto_field()
    title = ma.auto_field()

singular_job_schema = JobSchema()
#plural_job_schema = JobSchema(many=True)

class AvailabilitySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Availability 

    id = ma.auto_field()
    start_time = ma.auto_field()
    end_time = ma.auto_field()
    pass
singular_availability_schema = AvailabilitySchema()
#plural_availability_schema = AvailabilitySchema(many=True)


class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employee
    
    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    phone_number = ma.auto_field()
    job = ma.Nested(singular_job_schema)
    #start_time = ma.Nested(singular_availability_schema)
    #end_time = ma.Nested(singular_availability_schema)

singular_employee_schema = EmployeeSchema()
plural_employee_schema = EmployeeSchema(many=True)

#class EmployeeJobSchema(ma.SQLAlchemySchema):
 #   class Meta:
  #      model = EmployeeJob
   # pass 
class Employees(Resource):
    def get(self):
        employee = Employee.query.all()
        response = make_response(
            plural_employee_schema.dump(employee),
            200,
        )
        return response
    def post(self):
        
        new_employee = Employee(
            first_name = request.form["first_name"],
            last_name = request.form["last_name"],
            email = request.form["email"],
            phone_number = request.form["phone_number"],
        )
        db.session.add(new_employee)
        db.session.commit()

        response = make_response(
            singular_employee_schema.dump(new_employee),
            201
        )
        return response
api.add_resource(Employees, ('/employee'))

class EmployeeByID(Resource):
    def get(self,id):
        response_json = singular_employee_schema.dump(Employee.query.filter_by(id=id).first())
        response = make_response(response_json,200,)

        return response
    
    def patch(self, id):
        employee = Employee.query.filter_by(id=id).first()
        data = request.get_json()
        for k,v in data.items():
            setattr(employee, k, v)
        
        db.session.commit()

        return singular_employee_schema.dump(employee), 200 
    def delete(self, id):
        employee = Employee.query.filter_by(id=id).first()
        db.session.delete(employee)
        db.session.commit()

        return {'message':'Employee deleted'},200
    
api.add_resource(EmployeeByID, ('/employee/<int:id>'))

if __name__ =='__main__':
    app.run(port=5000, debug=True)