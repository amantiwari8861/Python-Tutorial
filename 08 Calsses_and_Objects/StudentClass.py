class Student:
    id
    institute="Mega"  #instance variables
    marks=0 #instance variables
    def __init__(self,name,marks,stid): #parametrized constructor
        print("parameterized constructor called")
        self.id=100
        self.name=name
        self.marks=marks
        self.stid=stid

    def showDetails(self):
        print("id ",self.id,"the name is ",self.name,"stid is ",self.stid,"marks is",self.marks,"institute is ",self.institute)


# st1=Student()  #creted an object (instance of a class)
# print("institute is ",st1.institute)
# st1.showDetails()

student1=Student("aman",95,102)
student1.showDetails()

print("the name is ",student1.name)
print("the marks is ",student1.marks)
print("the stid is ",student1.stid)
print("the institute is ",student1.institute)