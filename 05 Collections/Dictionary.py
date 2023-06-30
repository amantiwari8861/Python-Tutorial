# d2={}
# d1=dict()

# user_details={"name":"Aman","aadhar":123456,5:"Five"}
# print("the user details is :",user_details)

# print(user_details.get("name"))
# print(user_details.get("5"))
# print(user_details.get(5))

# print(user_details.keys())
# print(user_details.values())
# print(user_details.items())

# userdict=user_details.copy()
# print(userdict)

# user_details.update({"name":"Aman Tiwari"})

# print(user_details)

# user_details.update({"Age":24})
# print(user_details)

# print("Aadhar Number:",user_details["aadhar"])

# user_details.pop(5)
# user_details.pop("name")

# print(user_details)
# #stack -> last in first out
# user_details.popitem()
# print(user_details)

# user_details.popitem()
# print(user_details)

# del user_details["name"]
# print(user_details)

# del user_details
# user_details.clear()
# print(user_details)


# for k in user_details:
#     print("-------------------------")
#     # print("key:",k) # for key
#     # print("value:",user_details[k]) # for value
#     print(k,"=",user_details[k])    

# print(user_details.items())

# for k,v in user_details.items():
#     print("-------------------------")
#     # print(k," ",v)
#     print("key :",k," value :",v)

user_details={
                "name":"Aman",
                "aadhar":123456,
                "address":{
                            "state":"UP",
                            "city":"noida",
                            "pincode":201301
                          },
                "skills":["C","C++","java","python"]
            }
# print(user_details)
# print(user_details["address"]["city"])

for k in user_details:
    if isinstance(user_details[k],dict):
        for nk in user_details[k]:
            print("\t",nk,":",user_details[k][nk])
    else:
        print(k,":",user_details[k])

