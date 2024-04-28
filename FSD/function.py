# there are 4 types of function :
#     no argument no return type
#     no argument with return type
#     with argument no return type
#     with argument and return type

# def greet():
#     print("Hello everyone!")

# res=greet()
# print(res)


# 1. no argument no return type
# def showCalculatorModelNo():
#     print("Casio calculator ")

# showCalculatorModelNo()


# 2.no argument with return type
# def whatIsValueOfPi():
#     return 3.14

# res=whatIsValueOfPi()
# print(whatIsValueOfPi())

#3. with argument no return type
# def printVolOfSphere(radius):
#     result=4/3*3.14*radius**3
#     print("The result is :",result)

# printVolOfSphere(2.5)

#4.  with argument and return type
# def cube(num):
#     return num**3

# print(cube(2))
# print(cube(3))
# print(cube(5))

# radius=2.5
# result=4/3*3.14*cube(radius)
# print("the result is ",result)

# create a function named powerFxn() and take 2 parameters named num,pow and return the result

def printVolOfSphere(radius,PI=3.14):
    result=4/3*PI*radius**3
    print("The result is :",result)

printVolOfSphere(2.5)

