import json


user_details = {
    "name": "Aman",
    "aadhar": 123456345678,
    "salary":12.5,
    "address": {
        "state": "UP",
        "city": "noida",
        "pincode": 201301
    },
    "skills": ["C", "C++", "java", "python", "etc"],
    "age":None
}

# userStr=json.dumps(user_details)
# print(userStr)
# print(type(userStr))

# userObj=json.loads(userStr)
# print(userObj)
# print(type(userObj))


# with open("10 json/users.json", "w") as file:
#     json.dump(user_details, file, indent=4)

# with open("10 json/users.json", "r") as file:
#     data = json.load(file)

# print(data)


# # Write JSON
# try:
#     with open("10 json/users.json", "w") as file:
#         json.dump(user_details, file, indent=4)
#     print("Data written successfully.")

# except (PermissionError, TypeError, OSError) as e:
#     print(f"Error while writing JSON: {e}")

# # Read JSON
# try:
#     with open("10 json/users.json", "r") as file:
#         data = json.load(file)

#     print("Data read successfully:")
#     print(data)

# except FileNotFoundError:
#     print("Error: File not found.")

# except json.JSONDecodeError:
#     print("Error: Invalid JSON format.")

# except (PermissionError, OSError) as e:
#     print(f"Error while reading JSON: {e}")

