import json

class Person(object):
    """Create the base attributes of a person"""
    def __init__(self, name, age,email):
        self.name=name
        self.age=age
        self.email=email

class Student(Person):
    """Create the base attributes of a person"""
    def __init__(self, name, age,email,student_id):
        Person.__init__(self, name, age,email)
        self.student_id=student_id

def Saver(object):
    filename='Student.json'
    with open(filename,'w') as f:
        json.dump(Student,f)

def display_JSON(json):
    
