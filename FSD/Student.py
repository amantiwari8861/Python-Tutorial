class Student:
    def __init__(self,name=None):
        self.name=name
        self.inputData()
        
    def inputData(self):
        self.n=int(input("enter no. of subjects:"))
        self.marks=[]
        for i in range(self.n):
            self.marks.append(float(input("enter marks "+str(i+1)+":")))
        # print(self.marks)

    def showPercentage(self):
        total=0
        for i in self.marks:
            total+=i
        print(f"{self.name} got {total} marks having {total/len(self.marks)}% ")

stu1=Student("Aman")
stu1.showPercentage()

stu2=Student()
stu2.showPercentage()

stu3=Student("Xyz")
stu3.showPercentage()