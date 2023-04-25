# import math
# def volOfSphere(radius):
#     return 4/3*math.pi*radius**3

# print(volOfSphere(2.5))
# print(volOfSphere(5.5))
# print(volOfSphere(2.8))
# print(volOfSphere(8.5))
# print(volOfSphere(9))

def sumOfN(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum

result=sumOfN(10)
print("The Result is",result)
# or 
print("The Result is ",sumOfN(10))
print("The Result is ",sumOfN(7))
print("The Result is ",sumOfN(12))
print("The Result is ",sumOfN(100))
print("The Result is ",sumOfN(5000))
