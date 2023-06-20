num=int(input("enter a num :"))

revnum=0
while num !=0:
    value=num % 10
    revnum=revnum*10+value
    num = int(num/10)

print("ur reverse no is",revnum)