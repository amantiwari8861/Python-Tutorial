# def counting(num):
#     print("num = ",num)
#     counting(num-1)
# counting(10)

# def counting(num):
#     print("num = ",num)
#     break
#     counting(num-1)
# counting(10)

# def counting(num):
#     if(num>0):
#         print("num = ",num)
#         counting(num-1)

# counting(10)


# def factorial(num):
#     if(num>0):
#         return num*factorial(num-1)
#     else:
#         return 1

# num=int(input("enter a number :"))
# result=factorial(num)
# print("the factorial is ",result)


def countFor(num):
    if(num<=10):
        print("num =",num)
        countFor(num+1)

countFor(1)