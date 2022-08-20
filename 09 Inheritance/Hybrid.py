class Mammals:
    def mammalProperty(self):
        print("we give birth to child and we r warm blooded ")

class BlackDog(Mammals):
    def BlackDogProperty(self):
        print("we are black in color ")

class WhiteDog(Mammals):
    def WhiteDogProperty(self):
        print("we are white in color ")


class BlackAndWhiteDog(BlackDog,WhiteDog):
    def BlackAndWhiteDogProperty(self):
        print("we are black and white in color ")


class GreyDog(BlackAndWhiteDog):
    def greyDogProperty(self):
        print("we are grey in color ")

d1=GreyDog()
d1.mammalProperty()
d1.BlackDogProperty()
d1.WhiteDogProperty()
d1.BlackAndWhiteDogProperty()
d1.greyDogProperty()

