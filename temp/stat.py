class Student:
    clg="ABC"
    @staticmethod
    def setClgName():
        Student.clg="Eshan"

stu=Student()
print(stu.clg)
stu.setClgName()
print(stu.clg)

stu1=Student()
print(stu1.clg)
