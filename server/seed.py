from faker import Faker
from app import app
from models import db, Employee, Job, Availability, EmployeeJob
import datetime
from faker.provider import DynamicProvider

restaurant_staff = DynamicProvider(
    job = ["server", "kitchen", "manager"]
)

fake = Faker()

fake.add_provider(restaurant_staff)
with app.app_context():
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
        job = fake.restaurant_staff() #join to employee in model
        employee.password_hash = employee.username + 'password'


        employee.append(employee)
    
    db.session.add_all(employee)
