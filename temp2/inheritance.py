class Employee:
    companyName="TCS"
    def __init__(self,empId=None,name=None,salary=None):
        self.empId=empId
        self.name=name
        self.salary=salary
    def showEmployeeDetails(self):
        print(f" Id:{self.empId} Name:{self.name} Salary:{self.salary} ")

class Intern(Employee):
    def __init__(self,eid,name,salary,workPerDay):
        super().__init__(eid,name,salary)
        self.workPerDay=workPerDay
        print("only ",workPerDay,"hrs task is assigned")

    def travelAllowance(self):
        print("getting travel allowance of 3000")

class Permanent(Employee):
    pass



# emp1=Employee(100,"Aniket",300000)
# emp1.showEmployeeDetails()

int1=Intern(100,"mehak",20000,4)
print(int1.companyName)
int1.showEmployeeDetails()
int1.travelAllowance()
