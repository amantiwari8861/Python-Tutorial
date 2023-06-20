num=int(input("enter a number:")) #let num=153

original=num
sum=0
while num>0:
    rem=num%10
    sum=sum+rem**3
    num=int(num/10)

if original==sum:
    print("Armstrong no.")
else:
    print("not an armstrong no.")





'''
    Psuedocode/Dry-run

step 1:





'''