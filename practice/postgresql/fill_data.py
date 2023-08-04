import random

from faker import Faker

from connect_db import session
from models import Student, Group

fake = Faker()


def add_group():
    groups = [Group(name=f"XA-{i}") for i in range(20)]
    # group = Group(name="XA-07")
    # session.add(group)
    session.add_all(groups)
    session.commit()
    print("Group was saved successfully.")
    session.close()


# add_group()


def add_user():
    students = [
        Student(fullname=fake.name(), group_id=random.randrange(1, 20))
        for i in range(300)
    ]
    # student = Student(fullname="Ariana", group_id=1)
    # session.add(student)
    session.add_all(students)
    session.commit()
    print("Student was saved successfully.")
    session.close()


add_user()
