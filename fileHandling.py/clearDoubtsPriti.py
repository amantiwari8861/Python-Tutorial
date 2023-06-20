# no argument no return type

# def greet():
#     print("good evening")

# greet()

# with argument no return type

# def multi(a,b):
#     print("the result is ",a*b)

# n1=int(input("enter the first no."))
# n2=int(input("enter the second no."))

# multi(n1,n2)

# no argument with return type

# def givePIvalue():
#     return 3.14

# print("the value of pi is ",givePIvalue())

# with argument and return type

l1=[10,20,30,40,50]

def sumAll(arr):
    sum=0
    for e in arr:
        sum+=e
    return sum

result=sumAll(l1)
print('the sum of all elements is ',result)



