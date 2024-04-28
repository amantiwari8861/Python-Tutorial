class Mammals:
    def mammalProperty(self):
        print("we give birth to child and we r warm blooded ")

class cats(Mammals):
    def catsProperty(self):
        print("we walks on 4 legs and we have a tail and omnivores")

class Tiger(cats):
    def tigerProperty(self):
        print("we r big in size and very powerful and national animal of india")

julie=Tiger()
julie.mammalProperty()
julie.catsProperty()
julie.tigerProperty()