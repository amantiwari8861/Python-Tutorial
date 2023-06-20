class Bird:
    def fly(self):
        print(" birds can fly ")

class Ostrich(Bird):
    def fly(self):
        print(" ostrich can't fly")

class Pigeon(Bird):
    def fly(self):
        print(" pigeon can fly ")


os=Ostrich()
pig=Pigeon()
b=Bird()

# os.fly()
# pig.fly()
# b.fly()

for bird in (os,pig,b):
    bird.fly()
