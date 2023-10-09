from faker import Faker
from app import app
from models import db, Employee, Job, Availability, EmployeeJob
import datetime
#from faker.providers import DynamicProvider
from faker.providers import BaseProvider

#restaurant_staff = DynamicProvider(
#    job = ["server", "kitchen", "manager"])

class DynamicProvider(BaseProvider):
    def restaurant_staff(self):
        return self.random_element(['server', 'kitchen', 'manager'])
    
fake = Faker()

fake.add_provider(DynamicProvider)

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

#need to use faker to append a random job to each employee. look into employee.job.append(job?)
        employee.job = job
    
        db.session.add_all(employee)
db.session.commit()
