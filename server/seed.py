from faker import Faker
from app import app
from models import db, Employee, Job, Availability, EmployeeJob
import datetime

fake = Faker()

with app.app_content():
    print("Deleting all records...")
    Employee.query.delete()
    Job.query.delete()
    Availability.query.delete()
    EmployeeJob.query.delete()

    print("Creating Staff...")

    plural_employee = [] 
    plural_username = []

    for i in range(20):

        username = fake.first_name()

        while username in username:
            username = fake.first_name()

        plural_username.append(username)

        employee = Employee(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone_number = fake.phone_number(),
        )
