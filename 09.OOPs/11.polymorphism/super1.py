class Primates:
    legs=2
    def eat(self):
        print("they eats only fruits and veggies")

class Human(Primates):
    def eat(self):
        super().eat() #calling superclass behaviour
        # self.eat()
        print("they eat both veg and non veg")
        # print("legs :",super().legs)#calling superclass attribute

h=Human()
h.eat()
