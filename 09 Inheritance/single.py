# when a child class gets the properties of it's parents or ancestors 
# then it is called inheritance.

class Mammals:
    def __init__(self):#constructor
        print("Mammal created")
        self.bloodType="Warm" # property = data = fields = attributes = variables
        self.reproduceMethod="Gives birth"

    def showMammalProperty(self): # behaviour = method = function
        print("we ",self.reproduceMethod," to child and we are ",self.bloodType,"blooded")

    def eat(self):
        pass

class Human(Mammals):
    legs=2
    def showHumanProperty(self):
        print("we walk on ",self.legs," legs ")

prashant=Human() # object means real world entity
prashant.showMammalProperty()
prashant.showHumanProperty()