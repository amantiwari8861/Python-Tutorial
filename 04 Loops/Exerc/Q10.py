

for i in range(5):
    for s in range(i):
        print(" ",end="")
    
    for j in range(5,i,-1):
        print("*",end="")
    print()
