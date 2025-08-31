# Loops 

# for i in range(1,10,2):
#     print(i," Hello Aman Sir")

# for i in range(1,-10):
# for i in range(10,-3,-1):
# for i in range(10,-3):
#     print(i," Hello Aman Sir")
# start=i=0  -> only 1 time

# condition=i<10
# condition=i>10
# increment=i+=1

noOfDigit=int(input("enter no. of digits :")) # 5
total=0
for i in range(noOfDigit): # 0 - 4
    num=int(input("enter no. "+str(i+1)+" : "))
    total+=num

print("Total=",total)

"""
            DRY-RUN (psuedocode)

    Step 1: i=0,total=0,noOfDigit=3
            i<noOfDigit
            0<3 True
            num=6
            total=total+num
            total=0+6
            total=6
    
    Step 2: i=1,total=6,noOfDigit=3
            1<3 T
            num=7
            total=6+7 => 13
    
    Step 3:i=2,total=13,noOfDigit=3
            2<3 T
            num=10
            total=13+10 => 23
    
    Step 4: i=3,total=23,noOfDigit=3
            3<3 False
            loop terminated!

"""