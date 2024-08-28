# A set is an unordered collection and no indexal access.
# Sets are mutable and have no duplicate elements.

# fruits={10,}
# fruits=set()  #empty set
# fruits={"Apple","Mango","Apple","Banana",10,78,54.55}

# print(fruits)

# print(fruits[0])  #sets are unordered, so it doesn't support indexing


# fruits.add("pineapple")
# print(fruits)

# fruits.remove("Banana")
# print(fruits)

# # the remove() method will raise an error if the specified item does not exist
# # , and the discard() method will not
# fruits.remove("Banana 2")
# fruits.discard("Banana 2")
# print(fruits)

# fruits.update(["custardapple","cherry"])
# fruits.update({"custardapple2","cherry2"})
# print(fruits)

fruits={"Apple","Mango","Apple","Banana",10,78,54.55}
# # # Remove all elements of another set from this set.
# fruits.difference_update(["custardapple","Mango","kashmiri apple"])
# print(fruits)
favourite_fruits={"Apple","Mango","litchi"}
# favourite_fruits=["custardapple","Mango","kashmiri apple"]
# # print('favourite fruits :',favourite_fruits)
# print("after difference :",fruits.difference(favourite_fruits)) # A-B
# print("after difference :",favourite_fruits.difference(fruits)) # B-A
# print(fruits)
# print(favourite_fruits)

print("after intersection :",fruits.intersection(favourite_fruits)) # A intersection B
print("after intersection :",favourite_fruits.intersection(fruits)) # A intersection B
# print("union :",fruits.union(favourite_fruits))
print(" is not Any Common element :",fruits.isdisjoint(favourite_fruits)) #is none of the items are present in both sets (Return True if two sets have a null intersection.)
# vegetables={"potato","spinach"}
vegetables={"potato","spinach"}
print(" is not Any Common element :",fruits.isdisjoint(vegetables))


# A={1,2,3,4,5}  
# B={1,2,3}
# C={1,2,3,8,9}
# print(A.issubset(B)) # is all Element of A is present in B
# print(B.issubset(A))
# print(A.issuperset(B)) # is All elements of B present in A

# print(A.symmetric_difference(C)) # 

# fruits={"Apple","Mango","Apple","Banana",10,78,54.55}
# favourite_fruits=["custardapple","Mango","kashmiri apple"]

# remaining=fruits.difference_update(favourite_fruits)
# print(remaining)
# print(fruits)
# print("---------------------------------------")
# remaining=fruits.difference(favourite_fruits)
# print(remaining)
# print(fruits)