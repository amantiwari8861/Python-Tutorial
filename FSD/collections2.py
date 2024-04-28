# mylist=["1","xyz","Abc","abc","XYZ"]
# mylist.sort()
# mylist[0]="hello"
# print(mylist)

# A={10,20,30,10,20,40}
# print(A)
# # A[0]=99
# A.add(56)
# A.remove(20)
# print("A=",A)
# B={10,34,78,98}
# print("B=",B)
# print(A.difference(B))

# my_Data=(10,20,30,40,10,30)

# print(my_Data)
# print(my_Data[0])
# my_Data[0]=78

# aadharCard=["AMan","xyz",9891062743,"ca",28]
aadharCard={
    "name":"Aman","mobileNo":9891062743,"job":"Developer","isMarried":False,
    "skills":["MEAN","MERN","Java FSD","etc"],
    "address":{
        "city":"Noida",
        "pincode":201301,
        "country":"India"
        },
    "name":"xyz"
    }

# print(aadharCard)
# print(aadharCard[0])
# print(aadharCard["name"])
# print(aadharCard["skills"])
# print(aadharCard["skills"][0])
# print(aadharCard["address"])
# print(aadharCard["address"]["city"])

# for k in aadharCard:
#     print(k)

# for k in aadharCard:
#     # print(k,":",aadharCard[k])
#     print(k,type(aadharCard[k]),end="")
#     print(isinstance(aadharCard[k],list))

# for key in aadharCard:
#     if isinstance(aadharCard[key],dict):
#         print(key,":{")
#         for nestedKey in aadharCard[key]:
#             print("\t",nestedKey,":",aadharCard[key][nestedKey])
#         print("\t}")
#     else:
#         print(key,":",aadharCard[key])

# create add,sub,multiply,divide,volOfSphere,powerFxn,volOfCylinder
# function and perform all the operations

# can we store list of employees ?
# allEmployees=[
#     {"name":"Aman","Age":28},
#     {"name":"Naman","Age":26},
#     {"name":"Raman","Age":29},
#     {"name":"Xyz","Age":35},
#     ]

# take 5 foods data(like name,calories,etc) in an array of dictionary and calculate total calories of all foods.

# aadharCard.update({"mobileNo":98965766876})
# aadharCard.update({"Age":28})
# # aadharCard.clear()
# aadharCard.pop("name")
# aadharCard.pop("Age")
# aadharCard.pop("mobileNo")

# print(aadharCard)


# hello={}
# hello=set()
# hello=dict()
# print(type(hello))

key=input("enter key:")
val=input("enter value:")

userDetails={}
userDetails.update({key:val})

print(userDetails)
# OOPs -> object oriented programming system
Class 
Object 
    