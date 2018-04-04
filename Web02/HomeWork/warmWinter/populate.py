from models.customer import Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()
fake = Faker()
for i in range(30):
    print("Saving service", i + 1, "...")
    new_custormer = Customer(name = fake.name(),
                          gender = randint(0, 1),
                          email = fake.safe_email(),
                          phone = fake.phone_number(),
                          job = fake.job(),
                          company = fake.company(),
                          contacted = choice([True,False])
    )
    new_custormer.save()
