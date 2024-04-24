# overloading constructor in python

class Student:
    # we can't do this
    def __init__(self):
        print("student created")

    def __init__(self, id):
        self.id = id

    def __init__(self, id, name, course):
        print("student created")
        self.id = id
        self.name = name
        self.course = course

    def showDetails(self):
        print("Student id is :", self.id)
        print("Student Name is :", self.name)
        print("Student Course is :", self.course)

# stu1 = Student()
# stu1.showDetails()

# stu2 = Student(101)
# stu2.showDetails()

stu3 = Student(102, "Aman Tiwari", "Devops")
stu3.showDetails()
