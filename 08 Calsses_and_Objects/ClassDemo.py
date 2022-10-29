#class is a set of objects which shares a common structure and behaviour

# OOPs : object oriented programming System
# software development methodology which relates to real world

# eg. if u want to make a car what will you do 
#     1.BluePrint
        # in bluepringt we have data(variables) and behaviour(functions)

#  how many cars we can build using same blue print ? Ans. Infinite
#  if both the cars are made of same blue print then i will be same or not ? Ans. Yes
# let we maked 2 cars from same blueprint one i gave u and 1 have taken
# then can i say to you that your car is also mine ? Ans. No
# bcz every car(object) have it's own identity(chasis no.,Registration No.) it can't be duplicate

# Object : instance of class 

a=10
# b="hii"
# bcz python is dynamically types programming language
# print(type(a))
# print(type(50))
# print(type("Hello"))
# here 50 is a object of int class and "Hello" is object of str class

class Car:
    model1="Bugati veygon"

#     def showDetails(self):
#         print("my car is ",self.model1)

car1=Car()
# car1.showDetails()
print(car1.model1)

car2=Car()
car2.model1="audi Q3"
# car2.showDetails()
print(car2.model1)