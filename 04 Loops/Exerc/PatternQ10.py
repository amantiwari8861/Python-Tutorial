# *****
#  ****
#   ***
#    **
#     *

for row in range(1,6):
    for space in range(1,row):
        print(" ",end="")
    for star in range(6,row,-1):
        print("*",end="")
    print()
