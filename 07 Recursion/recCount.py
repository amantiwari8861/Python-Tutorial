#recursion : when a function call it itself it is called recursion

# def counting(num):
#     print("num = ",num)
#     counting(num-1) #fxn is calling itself

# counting(10) #calling 1st time


# def counting(num):
#     print("num = ",num)
#     break #SyntaxError: 'break' outside loop
#     counting(num-1)
# counting(10)

# def counting(num):
#     if(num>0):  #Base condition
#         print("num = ",num)
#         counting(num-1)

# counting(10)

# def counting(num):
#     if(num<=10):
#         print("num = ",num)
#         counting(num+1)

# counting(1)


def counting(num):
    if(num<=10):
        print("num = ",num)
        if num==5:
            return
        counting(num+1)

counting(1)