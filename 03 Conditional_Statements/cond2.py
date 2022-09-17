""" if
if else
if elif .. else """

#  if 15>50 : #true block
#     print("15 is greater than 5")
#     print("hii")

#if else

# if 15>50 : #true block
#     print("15 is greater than 5")
#     print("hii")
# else:
#     print("50 is greater") 
""" 
num1=int(input("enter the num1 : "))
num2=int(input("enter the num2 : "))

if num1<num2 :
    print(num1," is less than ",num2)
else :
    print(num2," is less than ",num1)

 """
# elif example

# marks= int(input("enter the marks "))

# if marks >= 60 and marks<=100 :
#     print(" u got 1st division")
# elif  marks >= 50 and marks<60 :
#     print("u got 2nd division ")
# elif marks >=33 and marks<50 :
#     print(" u got 3rd division ")
# else:
#     print(" u r failed ")

#nested 
marks= int(input("enter the marks "))

if marks >= 60 and marks<=100 :
    print(" u got 1st division")
    if marks >80 :
        print(" u got 1 lac. scholarship ")
elif  marks >= 50 and marks<60 :
    print("u got 2nd division ")
elif marks >=33 and marks<50 :
    print(" u got 3rd division ")
else:
    print(" u r failed ")