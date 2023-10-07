from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    number = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'
    
class Job(db.Models):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return '<Job {self.title}>'
    
class EmployeeJob(db.Model): #Join Table
    __tablename__ = 'employee_job'

    employee_id = db.Column('employee_id', db.Integer, db.ForeignKey('employee.id'),primary_key= True)
    job_id = db.Column('job_id', db.Integer, db.Forgeignkey('job.id'), primary_key=True)

    def __repr__(self):
        return f'<EmployeeJob {self.employee.first_name} {self.employee.last_name} - {self.job.title}'

class Availability(db.Models):
    __tablename__ = 'availability'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Availability {self.first_name} {self.last_name} - {self.start_time} - {self.end_time}>'