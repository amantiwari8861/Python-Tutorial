
# for i in range(5):
#     for j in range(7):
#         print("*",end="")
#     print()

# for i in range(10,0,-1):
#     print(i)


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

for i in range(1,6):
    for j in range(6,i,-1):# 6>1 t 5>1 t 
        if i%2 ==0:
            print("*",end="")
        else:
            print("$",end="")
    print()