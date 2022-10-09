# A set is an unordered collection and no indexal access.
# Sets are mutable and have no duplicate elements.

# fruits={}
# fruits=set()
fruits={"Apple","Mango","Apple","Banana",10,78,54.55}

# print(fruits)

# # print(fruits[0])  #sets are unordered, so it doesn't support indexing
# fruits.add("pineapple")
# print(fruits)

# fruits.remove("Banana")
# print(fruits)
# # the remove() method will raise an error if the specified item does not exist
# # , and the discard() method will not
# fruits.discard("Banana")
# # fruits.remove("Banana")
# print(fruits)

fruits.update(["custardapple","cherry"])
# fruits.update({"custardapple2","cherry2"})
print(fruits)

# Remove all elements of another set from this set.
fruits.difference_update(["custardapple","Mango","kashmiri apple"])
print("All fruits :",fruits)

favourite_fruits={"Apple","Mango","litchi"}
# print('favourite fruits :',favourite_fruits)
# print("after difference :",fruits.difference(favourite_fruits)) # A-B
# print("after difference :",favourite_fruits.difference(fruits)) # B-A
# print(fruits)
# print("after intersection :",fruits.intersection(favourite_fruits)) # A intersection B
# print("union :",fruits.union(favourite_fruits))
# print(" is disjoint :",fruits.isdisjoint(favourite_fruits))
# vegetables={"potato","spinach"}
# print(" is disjoint :",fruits.isdisjoint(vegetables))


A={1,2,3,4,5}  
B={1,2,3}
C={1,2,3,8,9}
print(A.issubset(B)) # is all Element of A is present in B
print(A.issuperset(B)) # is All elements of B present in A

print(B.issubset(A))
print(A.symmetric_difference(C))

