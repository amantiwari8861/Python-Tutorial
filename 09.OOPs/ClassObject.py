"""
    Procedural programming
    function = procedure
    
    OOPs -> Object Oriented programming system
     -> software development methodology 
     -> which relates to real world
     -> language independent 

    Advantages of OOPs
    1. realistic modeling
    2. splitting the complex problem in sub problems and arrange that in heirarchy
    3. information hiding
    
    python -> purely object oriented scripting language

    
    OOP -> consists of classes and Objects
    what is class ?
    class : class is a set of object which shares a common structure and behaviour
    objects : real world entity
"""

# def greet():
#     print("Hello there")
# greet()

# 10000 lines 


class Building:  # blue-print
    # attributes = state = data = variable
    noOfFloors=0
    noOfRooms=0
    builder="Aman Builders Pvt. Ltd."

    def __init__(self): # constructor -> special type of function which is used to initialize the data members or the member functions of a class
        print("Building created by default constructor")
        self.noOfFloors=4
        self.noOfRooms=12
        self.colour="White"

    # behaviour = function = method
    def paint(self):
        print("painting",self.noOfFloors,"floor's",self.noOfRooms,"rooms which is built by",self.builder,"with",self.colour,"colour")

# anujKiBuilding=Building() # here Building() is used to call constuctor
# # print(anujKiBuilding.colour,anujKiBuilding.noOfFloors,anujKiBuilding.noOfRooms,anujKiBuilding.builder)
# anujKiBuilding.colour="Blue"
# anujKiBuilding.paint()


# komalKiBuilding=Building()
# komalKiBuilding.colour="Pink"
# komalKiBuilding.paint()

# every object has it's own unique identity 

# Building()
# Building().paint()
# Building()
# Building()



# Student -> 10000
class Student:
    def __init__(self,name=None,age=None):
        self.name=name
        self.age=age

    def showDetails(self):
        print("name :",self.name,"age :",self.age)

s1=Student("raj",22)
s2=Student("aman",26)
s3=Student("anuj",28)
s4=Student("hardik",27)
s5=Student("komal",30)

# students=[s1,s2,s3,s4,s5]
# for s in students:
#     s.showDetails()

s3.showDetails()



# class,object,default or parameterized constructor,
# 4 major pillars of oops
# 1.inheritance
# 2.polymorphism
# 3.abstraction
# 4.encapsulation