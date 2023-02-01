class Cat:
    def catsProperty(self):
        print("we walks on 4 legs and we have a tail and omnivores")

class Tiger(Cat):
    def tigerProperty(self):
        print("we r big in size and very powerful and national animal of india")

class Lion(Cat):
    def lionProperty(self):
        print("we r big in size and very powerful ")

class Liger(Lion,Tiger):
    def ligerProperty(self):
        print("Ligers have a tiger-like striped pattern,They enjoy swimming, which is a characteristic of tigers, and are very sociable like lions. ")

liger1=Liger()
liger1.catsProperty()
liger1.lionProperty()
liger1.tigerProperty()
liger1.ligerProperty()