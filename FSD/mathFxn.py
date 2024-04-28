import math
def inputData():
    num1=float(input("enter no. 1:"))
    num2=float(input("enter no. 2:"))
    return [num1,num2]

def add(inputs):
    return inputs[0]+inputs[1]

def sub(inputs):
    return inputs[0]-inputs[1]

def multi(inputs):
    return inputs[0]*inputs[1]

def divide(inputs):
    return inputs[0]/inputs[1]

def volOfsphere(radius):
    return 4/3*math.pi*radius**3
