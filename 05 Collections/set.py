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
# print(fruits)

# fruits.update(["custordapple","cherry"])
# print(fruits)

# fruits.difference_update(["custordapple","cherry","kashmiri apple"])
print("All fruits :",fruits)

favourite_fuits={"Apple","Mango","litchi"}
print('favourite fruits :',favourite_fuits)
vegetables={"potato","spinach"}
# print("after difference :",fruits.difference(favourite_fuits))
# print("after intersection :",fruits.intersection(favourite_fuits))
# print("union :",fruits.union(favourite_fuits))
# print(" is disjoint :",fruits.isdisjoint(favourite_fuits))
# print(" is disjoint :",fruits.isdisjoint(vegetables))


A={1,2,3,4,5}  
B={1,2,3}
C={1,2,3,8,9}
print(A.issubset(B)) # is all Element of A is present in B
print(A.issuperset(B)) # is All elements of B present in A

print(B.issubset(A))

print(A.symmetric_difference(C))

