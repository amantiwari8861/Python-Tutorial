class Car:
    def __init__(self): # non-parameterized constructor (default constructor)
        self.model="Bugatti chiron"   
        print("hello i am default constructor")

    def showDetails(self):
        print("my car is ",self.model)

c1=Car()   #instantiation -> the process of making object
c1.showDetails()
print("the model of this car is ",c1.model)

# c2=Car()   #instantiation -> the process of making object

#constructor : constructor is a special type of method which is used to
#  initialize the data members and member function of a class