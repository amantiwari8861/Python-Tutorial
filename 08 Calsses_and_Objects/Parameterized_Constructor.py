class Building:

    # def __init__(self):
    #     print("default constructor")
    #     self.institute="Mega"
    institute="Mega"
    def __init__(self,owner):
        self.owner=owner

    
# b=Building()
# b1=Building()
# b2=Building()
# b3=Building()
# b4=Building()
# print(b.institute)

b8=Building("Chandrajeet Singh")
print(b8.institute,"'s owner is ",b8.owner)

# Python does not support explicit multiple constructors, yet there are some ways 
# using which the multiple constructors can be achieved. If multiple __init__
#  methods are written for the same class, then the latest one overwrites all the previous constructors