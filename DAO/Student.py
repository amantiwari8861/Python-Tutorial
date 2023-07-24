class Student:
    def __init__(self,stid=None,name=None,phone=None,fees=None,isMarried=None,address=None):
        self.stid=stid
        self.name=name
        self.phone=phone
        self.fees=fees
        self.isMarried=isMarried
        self.address=address

    def showDetails(self):
        print(" ==============Student Details===============")
        print("Id :",self.stid)
        print("Name :",self.name)
        print("Fees :",self.fees)
        print("Address :",self.address)
        print("Phone :",self.phone)
        print("is married ? :",self.isMarried)