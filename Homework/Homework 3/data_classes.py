import json

class Person(object):
    """Create the base attributes of a person"""
    def __init__(self, name, age,email):
        self.name=name
        self.age=age
        self.email=email
    def convert_dict(self):
        return self.__dict__

class Student(Person):
    """Create the base attributes of a person"""
    def __init__(self, name, age,email,student_id):
        Person.__init__(self, name, age,email)
        self.student_id=student_id

def Saver(Student):
    filename='Student.json'
    with open(filename,'a') as f:
        json.dump(Student.convert_dict(),f,indent=4,)
        f.write('\n')
def display_JSON(json):
    with open('Student.json') as f:
        studentdata=json.load(f)
    print(json.dumps(studentdata,indent=4))
