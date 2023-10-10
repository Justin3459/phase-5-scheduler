from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref
from flask_migrate import Migrate

db = SQLAlchemy()

employee_job = db.Table('employee_job',
                        db.Column('employee_id', db.Integer, db.ForeignKey('employee.id')),
                        db.Column('job_id', db.Integer, db.ForeignKey('job.id'))
)

class Job(db.Model):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Job {self.title}>'
    
class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)

    job = db.relationship('Job', secondary=employee_job, backref=db.backref('employee'))

    username = db.Column(db.String(),unique=True, nullable=False)
    password = db.Column(db.String(),nullable=False)

    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'

class EmployeeJob(db.Model):
    __tablename__ = 'employeesjobs'

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), primary_key=True)

class Availability(db.Model):
    __tablename__ = 'availability'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Availability {self.employee.first_name} {self.employee.last_name} - {self.start_time} - {self.end_time}>'
