# polymorphism : poly -> many  morphs -> forms
class Bird:
    def fly(self):
        print(" birds can fly ")
class Ostrich(Bird):
    # pass
    def fly(self):
        print(" ostrich can't fly it runs")
class Pigeon(Bird):
   pass

b=Bird()
# b.fly()

os=Ostrich()
# os.fly()

pi=Pigeon()
# pi.fly()

for brd in (os,pi,b):
    brd.fly()
