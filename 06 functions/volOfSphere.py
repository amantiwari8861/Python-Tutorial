# 4/3*pi*r*r*r
def volOfSphere(r):
    return 4/3*3.14*r**3


radius=float(input("enter the radius"))

result=volOfSphere(radius)
print("the volume of sphere is ",result)
print("the volume of sphere is ",volOfSphere(3.2))
print("the volume of sphere is ",volOfSphere(5))
print("the volume of sphere is ",volOfSphere(7.2))

# Advantages of Fxn :
# 1.reusability
# 2.modularity
# 3.increase readibiility
# 4.decrease complexity
