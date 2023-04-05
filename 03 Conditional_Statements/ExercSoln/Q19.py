id=input("Enter ur id:")
unit=int(input("enter ur unit:"))

if unit>=0 and unit<200:
    amount=unit*4.20
elif unit>=200 and unit<400:
    amount=unit*6.50
elif unit>=400 and unit<600:
    amount=unit*8.80
elif unit>=600:
    amount=unit*14
else:
    print("invalid unit !")

# print("amount = ",amount)

if amount>2000:
    print("15% surcharge will be added i.e ",amount*15/100)
    amount=amount+amount*15/100

if amount<200:
    amount=200
    print("minimun bill of 200 is mandatory")

print("the final amount is ",amount,"to pay!")