# Install necessary modules
# Command to install Pickle: pip install pickle-mixin
# Command to install JSON: No installation required, JSON is a built-in module in Python

import pickle
import json

# Define a class
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
obj = MyClass("John", 30)

# Serialize and store the object using Pickle
with open('object.pkl', 'wb') as file:
    pickle.dump(obj, file)

# Serialize and store the object using JSON
with open('object.json', 'w') as file:
    json.dump(vars(obj), file)

# Deserialize the object using Pickle
with open('object.pkl', 'rb') as file:
    obj_pkl = pickle.load(file)

# Deserialize the object using JSON
with open('object.json', 'r') as file:
    data_json = json.load(file)
    obj_json = MyClass(**data_json)

# Print the deserialized objects
print("Deserialized object from Pickle:", obj_pkl.name, obj_pkl.age)
print("Deserialized object from JSON:", obj_json.name, obj_json.age)
