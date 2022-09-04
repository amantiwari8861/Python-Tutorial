# num1=10
# num2=20
# num3=num1+num2
# print(num3)

#or
# num1=10,num2=20,num3  #not allowed in python
num1,num2=10,20
num3=num1+num2
print(num3)
print(type(num3))
#or
print("the sum of num1 and num2 is ",num3)
#or
print("the sum of ",num1," and ",num2," is ",num3)

print("the sum of "+str(num1)+" and "+str(num2)+" is "+str(num3))