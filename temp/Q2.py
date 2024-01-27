total=0
for i in range(1,10+1,-1):
    total+=i
    # print(i,end="")
    # if i<10:
    #     print(",",end="")
    
print("\nThe total is :",total)


'''
    PsuedoCode (false code/dry-run)

    Step 1:  total=0 ,i=1
            i<11 True
            total=total+i
            total=0+1 => 1

    Step 2: total=1 ,i=2
            2<11 True
            total=1+2 =>3


    Step 11: total=55,i=11
            11<11 False loop terminated


'''