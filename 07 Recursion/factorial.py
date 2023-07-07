##e.g. 5! = 5*4*3*2*1 =120

def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

num=int(input("enter a number :"))
result=factorial(num)
print("the factorial is ",result)


# H.w   make fibonnaci series
# 0 1 1 2 3 5 8 13 . . . 