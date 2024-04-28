class Car:
    company='Bugati'
    color="black"
    modelNo=""

    def accelerate(self,xyz):
        print("Model No. is :",self.modelNo," ",xyz)

satyamKicar=Car()
satyamKicar.modelNo="chiron"
satyamKicar.accelerate(10)
print(satyamKicar.company)
print(satyamKicar.color)
print(satyamKicar.modelNo)

print("*"*40)

aniketKicar=Car()
aniketKicar.modelNo="kuch nahi"
aniketKicar.accelerate(10)
print(aniketKicar.company)
print(aniketKicar.color)
print(aniketKicar.modelNo)