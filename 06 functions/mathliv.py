num=int(input("enter the number:"))
power=int(input("enter the power:"))

i,sum=1,1
while(i<=power):
    sum=sum*num
    i+=1

print("the power is ",sum)
result1=pow(num,power)
print("using math.pow() ",result1)
print("using math.pow() ",pow(5,3))
print("using math.pow() ",pow(3,4))
print("using math.pow() ",pow(2,8))
