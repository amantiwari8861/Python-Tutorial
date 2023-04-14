num=int(input("enter a number: "))

count=0
for i in range(1,num+1):
    if(num%i==0):
        # print(num," ",i," se perfectly kat gaya")
        count+=1

if count>2:
    print(num,"is not a prime no.")
else:
    print(num,"is a prime no.")