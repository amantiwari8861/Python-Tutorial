# class Building:
#     builder="Aman builders pvt. ltd."
#     rooms=0

#     def setval(self,rooms):
#         pass
#         # self.rooms=rooms 
#     def showBuildingDetails(self):
#         print("Builders ",self.builder)
#         print("Rooms ",self.rooms)

# buildingObj=Building() # instantiation 
# buildingObj.setval(50)
# buildingObj.showBuildingDetails()

class Building:
    builder="Aman builders pvt. ltd."
    # def __init__(self):
    #     print("constructing the building....")
    def __init__(self,rooms,floors,color="White"): #parameterized connstructor
        self.rooms=rooms
        self.floors=floors
        self.color=color
        print(f"rooms:{rooms} floors:{floors} color:{color}")
    def showBuildingDetails(self):
        print("Builders ",self.builder)
        print("Rooms ",self.rooms)
        print("floors ",self.floors)
        print("color ",self.color)
buildingObj=Building(100,5)
buildingObj.showBuildingDetails()

