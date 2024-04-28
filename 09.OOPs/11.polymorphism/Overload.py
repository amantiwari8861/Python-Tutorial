class Shape:
    def __init__(self,length=None,height=None,width=None,radius=None):
        # print("4 parameterized constructor")
        self.length=length
        self.height=height
        self.width=width
        self.radius=radius
    
    def __str__(self):
        return f"length {self.length} height {self.height} width {self.width} radius {self.radius} "

line=Shape(5)
line1=Shape(5,30)
line2=Shape(5,30,20)
line3=Shape(10,5,16,78)

print("line :",line)
print("line 1:",line1)
print("line 2:",line2)
print("line 3:",line3)