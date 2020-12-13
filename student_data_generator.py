import numpy as np
import pandas as pd

from faker import Faker
from datetime import date
from collections import OrderedDict

print("Starting Script\n")

fake = Faker("en_CA")

def create_student(n):
    students = []
    for _ in range(0, n):
        students.append(fake.profile(fields=("name", "address", "mail")))

    return students

def create_gender(n):
    gender = []

    for _ in range(0, n):
        gender.append(fake.random_element(elements=(OrderedDict([("male", 0.49), ("female", 0.49), ("other", 0.01)]))))

    return gender

def create_DOB(n):
    birthdates = []

    for _ in range(0,n):
        birthdates.append(fake.date_of_birth(minimum_age=18, maximum_age=30))

    return birthdates



def create_major(n):
    major = []
    for _ in range(0,n):
        major.append(fake.random_element(elements=("Finance", "Accounting", "Marketing", "History", "Psycology",
                                                     "Philosophy", "Biology", "Engineering", "Physics", "LGBTQ2+ Studies")))

    return major

def year_of_study(n):
    yos = []

    for _ in range(0, n):
        yos.append(np.random.randint(1,6))

    return yos



def grade_average(n):
    gpa = []

    for _ in range(0, n):
        gpa.append(round(np.random.uniform(0.5,0.99), 4))

    return gpa

def create_job(n):
    job = []

    for _ in range(0, n):
        job.append(fake.random_element(elements=("Part-Time - Internship", "Part-Time - Other", "Full-Time", "Unemployed")))

    return job

def create_living_situation(n):
    liv_sit = []

    for _ in range(0, n):
        liv_sit.append(fake.random_element(elements=("On Campus", "Off Campus", "With Parents", "Remote")))

    return liv_sit


def create_extra_ciriculars(n):
    extras = []

    for _ in range(0, n):
        extras.append(fake.random_elements(elements=("Intramurals", "Varsity", "Student Club", "Fraternity/Sorority"), unique = True))

    return extras

def calculate_age(birthdate):
    today = date.today()

    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def create_dataset(n):

    students = create_student(n)
    gender = create_gender(n)
    dob = create_DOB(n)
    major = create_major(n)
    yos = year_of_study(n)
    gpa = grade_average(n)
    job = create_job(n)
    living = create_living_situation(n)
    extcir = create_extra_ciriculars(n)


    df = pd.DataFrame.from_dict(students)
    df["gender"] = gender
    df["D.O.B"] = dob
    df["age"] = df["D.O.B"].apply(calculate_age)
    df["major"] = major
    df["Year"] = yos
    df["gpa"] = gpa
    df["employment"] = job
    df["living situation"] = living
    df["extra ciriculars"] = extcir
    
    df.to_csv("Student_Data.csv")
    

create_dataset(1000)

