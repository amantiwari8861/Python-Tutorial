class Mammals:
    def mammalProperty(self):
        print("we give birth to child and we r warm blooded ")


class Human(Mammals):
    def humanProperty(self):
        print("we walk on two legs ")



prashant=Human()
prashant.mammalProperty()
prashant.humanProperty()