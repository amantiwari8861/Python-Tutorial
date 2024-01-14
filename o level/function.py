# function : set of statements that performs a specific task 
# modularity (independent to each other )
# loose coupling(low dependency)
# reusability
# decrease complexity
# increase readibility

#inbuilt function(pre-defined)
#user defined

# no argument(parameter) no return type 
# no argument with return type 
# with argument no return type
# with argument and return type 

num=sum([10,20])  #here a list of [10,20] is arguments(parameter) here 30 is return value
# print(num)
# print(sum([10,30]))


# def type1():
#     print("Hello i am no argument no return type function")

# type1()  #calling of function


# def type2(a,b,c=5):
#     print("the sum is ",(a+b+c))

# sum1=type2(10,20) #calling of function
# print(sum1)


# def type3():
#     a,b=10,20
#     c=a+b
#     return c

# result=type3()
# print("the result is ",result)

# def type4(num,p):
#     res=1
#     for i in range(p):
#         res*=num
#     return res

# result=type4(2,7)
# print("the result is ",result)

# print(type4(7,2))
# print(type4(7,3))
# print(type4(2,5))
# print(type4(3,3))
# print(type4(4,3))

modi=56 #global variable

def sumOfNumbers(*numbers):
    # print(type(numbers))
    """ this function is used for adding n numbers"""
    print(modi)
    sum1=0  #local variable
    for num in numbers:
        sum1+=num
    return sum1

result=sumOfNumbers(10,20,30,40,50,56,84,98)
print("The result is ",result)

# print(sum1)
print(modi)