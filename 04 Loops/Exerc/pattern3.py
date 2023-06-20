'''

*****
 ****
  ***
   **
    *

'''

for i in range(5): #row
    for j in range(i):
        print(" ",end="")
    for k in range(5,i,-1):
    # for k in range(5-i,0,-1):
        print("*",end="")
    print()


