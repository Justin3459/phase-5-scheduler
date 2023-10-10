from faker import Faker
from app import app
from models import db, Employee, Job, Availability, EmployeeJob
import datetime
from faker.providers import BaseProvider

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
        username = fake.first_name() + fake.last_name()

        while username in username:
            username = fake.first_name() + fake.last_name()
            break

        plural_username.append(username)

        employee = Employee(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone_number = fake.phone_number(),
            username = username,
            password = 'password'
        )

        job = Job(
            title = fake.restaurant_staff()
        )
        #employee.password = 'password'
        #employee.username = username

        
        db.session.add(employee)
        db.session.add(job)
        db.session.commit()

        employee_job = EmployeeJob(
            employee_id=employee.id,
            job_id=job.id
        )
        db.session.add(employee_job)
        db.session.commit()
        print(employee, employee_job, job)
print('complete')
