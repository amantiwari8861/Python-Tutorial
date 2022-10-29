# import calcLib
import calcLib as lib
# from calcLib import add
# from calcLib import add as sum

size=int(input("enter the size of total numbers :"))
numbers=list()
for i in range(size):
    numbers.append(float(input("enter "+str(i+1)+" number :")))

# print(numbers)
# result=calcLib.add(numbers)
# result=sum(numbers)

op=input("enter operation :")
result=0
if (op=='+'):
    result=lib.add(numbers)
elif (op=="-"):
    result=lib.sub(numbers)
elif (op=="*"):
    result=lib.multi(numbers)
elif (op=="/"):
    result=lib.div(numbers)
else:
    print("operation not defined")

print("the result is ",result)