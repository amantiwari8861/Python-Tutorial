class Student:
    name=""
    id=0
    DOB=""
    institute=""

    # def __init__(self,institute="Mega",dob):  #error
    def __init__(self,dob,institute="Mega"):
        self.institute=institute
        self.DOB=dob

    def setNameAndId(self,name,id):
        self.id=id
        self.name=name

    def showDetails(self):
        print("id :",self.id)
        print("name :",self.name)
        print("DOB :",self.DOB)
        print("institute :",self.institute)

s1=Student("22/4/1999")
s1.setNameAndId("Aman",113114)
s1.showDetails()

        

