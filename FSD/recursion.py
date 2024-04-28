# def printNum(num):
#     print("num=",num)
#     if(num==5):
#         # break
#         return
#     printNum(num+1)

# print("before rec")
# printNum(1)
# print("after rec")


def count(num):
    if num<10:
        print("num=",num)
        count(num+1)
    # else:
    #     print("returning....")
    #     return
count(1)

# def factorial(num):
#     if num==0 or num==1: # base condition
#         return 1
#     else:
#         return num*factorial(num-1)
# result=factorial(5)
# print("the factorial is ",result)