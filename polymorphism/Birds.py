# polymorphism : poly -> many  morphs -> forms

class Bird:
    def fly(self):
        print(" birds can fly ")

class Ostrich:
    def fly(self):
        print(" ostrich can't fly it runs")

class Pigeon:
    def fly(self):
        print(" pigeon can fly ")


os=Ostrich()
pi=Pigeon()
b=Bird()

# os.fly()
# pig.fly()
# b.fly()

for brd in (os,pi,b):
    brd.fly()
