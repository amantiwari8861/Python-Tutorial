num=int(input("enter a number: "))

# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         # print(num," ",i," se perfectly kat gaya")
#         count+=1

# if count>2:
#     print(num,"is not a prime no.")
# else:
#     print(num,"is a prime no.")

isPrime=True
i=2
while i<num:
    if(num%i==0):
        # print(num,"/",i," se perfectly kat gaya")
        isPrime=False
    # else:
        # print(num,"/",i," se perfectly nahi kata")
    i+=1
    
if isPrime:
    print("it is a prime no.")
else:
    print("not a prime no.")    
