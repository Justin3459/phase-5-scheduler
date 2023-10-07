from flask import Flask, request, make_response
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Employee, Job, EmployeeJob, Availability

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scheduler.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
ma = Marshmallow(app)

class EmployeeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Employee
    
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    phone_number = ma.auto_field()

singular_employee_schema = EmployeeSchema()
plural_employee_schema = EmployeeSchema(many=True)

class Employee(Resource):
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
    
    class EmployeeByID(Resource):
        def get(self,id):
            response_json = singular_employee_schema.dump(Employee.query.filter_by(id=id).first())

            response = make_response(response_json,200,)
            return response

class JobSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Job
    
    title = ma.autofield()
singular_job_schema = Job()
plural_job_schema = Job(many=True)

class EmployeeJobSchema(ma.SQLAlchemySchema):
    class Meta:
        model = EmployeeJob
    
    pass 

class AvailabilitySchema(ma.SQLAlchemySchema):
    pass