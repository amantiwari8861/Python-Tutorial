""" 
    Write a program in python to calculate and print the Electricity bill of a given customer. The customer id, and unit consumed by the user should be taken from the keyboard and display the total amount to pay to the customer. The charge are as follow : 

    Unit	Charge/unit
    upto 199	@4.20
    200 and above but less than 400	@6.50
    400 and above but less than 600	@8.80
    600 and above	@14.00
    If bill exceeds Rs. 2000 then a surcharge of 15% will be charged and the minimum bill should be of Rs. 200/-
"""

unit=float(input("enter unit consumed:"))

amount=0
if (unit-200)>=0:
    amount=200*4.20
    print("charge applied:",4.20)
if unit>=200 and unit<400:
    amount+=(unit-200)*6.50
    print("charge applied at ",(unit-200),"is",6.50)

# elif unit>=400 and unit<600:
#     amount=unit*8.80
#     print("charge applied:",8.80)
# elif unit>=600:
#     amount=unit*14.0
#     print("charge applied:",14.0)
# else:
#     print("invalid unit!")
#     exit(1)

# print("Expected Amount :",amount)
# if amount>2000:
#     print("15% surcharge applied:",amount*0.15)
#     amount+=amount*0.15

# if amount<200:
#     amount=200
#     print("minimum meter charge is 200")

print("Net Amount to Pay :",amount)