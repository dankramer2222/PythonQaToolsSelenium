import random

from data.data import Person
from faker import Faker

faker = Faker()
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name(),
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        age=random.randint(18, 70),
        salary=random.randint(4000, 8000),
        department=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address(),

    )
