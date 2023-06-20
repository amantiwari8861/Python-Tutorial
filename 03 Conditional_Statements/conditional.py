""" conditional statements 
1. if 
2. if-else 
3. if elif . . . else  
4. nested if
"""

age = int(input("Enter your age : "))

# if age >=18: #true block
#     print("You are eligible to vote")
#     print("Thank You Visit Again!")
# #  print("hii") #error space are not same
# print("hii i am out of the if block") 

# if age >= 18:  # true block
#     print("You are eligible to vote")
#     print("Thank You Visit Again!")
# else:  # else block
#     print("You are not eligible to vote")
#     print("Sorry! for this!")

#elif

# if age>=60:
#     print("senior citizens get 1000 for voting")
# elif age>=26:
#     print("u will get 500 for voting")
# elif age>=18:
#     print("u will get 1 frooti and 1 ladoo")
# else:
#     print("go home and sleep")

if age>=60:
    print("senior citizens get 1000 for voting")
    if age>=90:
        print("greet him/her on stage")
    elif age>=70:
        print("greet them personally")
    else:
        print("one set of safari suit")
elif age>=26:
    print("u will get 500 for voting")
elif age>=18:
    print("u will get 1 frooti and 1 ladoo")
else:
    print("go home and sleep")



# marks = int(input("Enter your marks : "))

# if marks>=90 and marks<=100:
#     print("u got admission in DU")
# elif marks>=80 and marks<90:
#     print("u got admission in IPU")
# elif marks>=60 and marks<80:
#     print("u got admission in private university")
# elif marks>=33 and marks<60:
#     print("u got admission in ignou")
# else:
#     print("sell tea!")


# if marks >= 90 and marks <= 100:
#     print("u got admission in DU")
#     if marks >= 97:
#         print("u got CS Branch")
#         if marks == 100:
#             print("u got Scholarship of Rs.1,00,000")
#     elif marks >= 95:
#         print("u got EC Branch")
#     elif marks >= 93:
#         print("u got MEC Branch")
#     else:
#         print("u got Civil branch")
# elif marks >= 33 and marks < 90:
#     print("u got admission in other university")
# else:
#     print("sell tea!")
