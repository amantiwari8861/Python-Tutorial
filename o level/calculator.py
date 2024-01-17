import calcmodule as cm

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
result=0
choice=input("enter ur choice:")

if choice=="+":
    result=cm.add(num1,num2)
elif choice=="-":
    result=cm.sub(num1,num2)
elif choice=="*":
    result=cm.multi(num1,num2)
elif choice=="/":
    result=cm.divide(num1,num2)
elif choice=="vos":
    r=float(input("enter radius"))
    result=cm.volOfSphere(r)
else:
    print("invalid choice!")

print("the result is ",result)