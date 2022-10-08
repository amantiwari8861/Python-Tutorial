# d1=dict()
# print(d1)
# d2={}

user_details={"name":"Aman","addhar":123456,5:"Five"}
print("the user details is :",user_details)

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

# user_details.update({"Age":23})
# print(user_details)

# print("aadhar :",user_details["addhar"])

# user_details.pop(5)

# print(user_details)
#stack -> last in first out
# user_details.popitem()
# print(user_details)
# user_details.popitem()
# print(user_details)

# del user_details["name"]
# print(user_details)

# del user_details
user_details.clear()
print(user_details)


for e in user_details:
    print(e) # for key
    print(user_details[e]) # for value
    

# for k,v in user_details.items():
#     print("key :",k," value :",v)

# user_details={
#                 "name":"Aman",
#                 "addhar":123456,
#                 "address":{
#                             "state":"UP",
#                             "city":"noida",
#                             "pincode":201301
#                           }
#             }
# print(user_details)
# print(user_details["address"]["city"])
