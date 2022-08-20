class AquaticAnimal:
    def AquaticAnimalProperty(self):
        print("we can live in water")

class TerrestrialAnimal:
    def terrestrialAnimalProperty(self):
        print("we can live in land")

class Amphibians(AquaticAnimal,TerrestrialAnimal):
    def amphibiansProperty(self):
        print("we can live on both")
        print("we have respiratory organs like gills, lungs, buccopharyngeal membrane and the skin. ")

frog=Amphibians()
frog.AquaticAnimalProperty()
frog.terrestrialAnimalProperty()
frog.amphibiansProperty()


