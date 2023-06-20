# for i in range(1,5):
#     print("\nworking task ",i)
#     for j in range(1,4):
#         print(" subtask",j,"   ",end="")

# *****
# *****
# *****
# *****

# for i in range(1,5):
#     for j in range(1,6):
#         print("*",end="")
#     print()   # equals to \n


# print("hello",end="")
# print("Aman")

# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(1,i+1): # 1<1+1
#         print("*",end="")
#     print()

# *****
# ****
# ***
# **
# *

for row in range(1,6):
    for col in range(6,row,-1):
        print("*",end="")
    print()