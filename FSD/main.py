from mathFxn import add,inputData,volOfsphere,sub,multi,divide
# import mathFxn
# import mathFxn as calc
# from mathFxn import *
# import math

op=input("enter operation:")

if op=="+":
    # print("The sum is :",mathFxn.add(mathFxn.inputData()))
    # print("The sum is :",calc.add(calc.inputData()))
    print("The sum is :",add(inputData()))
elif op=="-":
    print("The sub is :",sub(inputData()))
elif op=="*":
    print("The multiply is :",multi(inputData()))
elif op=="/":
    print("The divide is :",divide(inputData()))
elif op=="volofsphere":
    print("volume of sphere is :",volOfsphere(float(input("enter radius:"))))
else:
    print("invalid operation")
# print(math.sqrt(2))

# tkinter(GUI) + pdbc(mysql) = project 
