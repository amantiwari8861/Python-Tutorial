# A set is an unordered collection.
# Sets are mutable and have no duplicate elements.

fruits={"Apple","Mango","Apple","Banana",10,78,54.55}

# print(fruits)

# print(fruits[0])  #sets are unordered, so it doesnot support indexing
# fruits.add("pineapple")
# print(fruits)

# fruits.remove("Banana")
# print(fruits)

# fruits.discard("Banana")
# fruits.remove("Banana")
print(fruits)

fruits.update(["custordapple","cherry"])
print(fruits)

fruits.difference_update(["custordapple","cherry","kashmiri apple"])
print(fruits)

