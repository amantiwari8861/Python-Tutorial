for row in range(1,6):
    for sp in range(5,row,-1):
        print(" ",end="")
    for c1  in range(1,row+1):
        print(c1,end="")
    for c2 in range(1,row):
        print(row-c2,end="")
    print()