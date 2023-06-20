class Mammals:
    def mammalProperty(self):
        print("we give birth to child and we r warm blooded ")

class cats(Mammals):
    def catsProperty(self):
        print("we walks on 4 legs and we have a tail and omnivores")

class Human(Mammals):
    def humanProperty(self):
        print("we walk on two legs ")

class dogs(Mammals):
    def dogsProperty(self):
        print("we walks on 4 legs and we have a tail and omnivores")
        print(" and we r human's best friend ")

class Tiger(cats):
    def tigerProperty(self):
        print("we r big in size and very powerful and national animal of india")

class Lion(cats):
    def lionProperty(self):
        print("we r big in size and very powerful ")

class Leopard(cats):
    def leopardProperty(self):
        print("we r big in size and very fast animal")


print("-----------------Tiger's Property--------------------")
julie=Tiger()
julie.mammalProperty()
julie.catsProperty()
julie.tigerProperty()
print("-------------------Dog's property-----------------")
tommy=dogs()
tommy.mammalProperty()
tommy.dogsProperty()
print("--------------------Human's Property------------------")
prashant=Human()
prashant.mammalProperty()
prashant.humanProperty()
print("----------------------Cat's Property-------------------")
c1=cats()
c1.mammalProperty()
c1.catsProperty()
