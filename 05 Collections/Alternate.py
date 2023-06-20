""" 
There are four collection data types in the Python programming language:

    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.

*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""



# vegList=[]
# vegList=list()
# vegList.append("Potato")
# vegList.append("Tomato")

# print(vegList)
# print(type(["potato","onion"]))

# vegSet={"onion","potato","onion","capsicum","Apple","banana"}
# print(vegSet)

# vegSet=set()
# vegSet.add("onion")
# print(vegSet)

# print(type({"onion","potato"}))


# marks=tuple(["onion","potato","onion","capsicum","Apple","banana"])
# print(marks)


# details=dict()
# details.update({"name":"Aman"})
# details.update({"marks":[23,45,67,89]})
# details.update({"veg":{"onion","potato"}})
# details.update({"fruits":("Apple","Banana")})
# details.update({"address":{"city":"noida","state":"UP"}})
# print(details)
# details=dict(name="aman",marks=(23,45,67,89))
# print(details)


# nameList=["ram",("aman","shubham")]
# nameList=["shyam",{"aman","shubham","aman"}]
# nameList=["ram",["aman","shubham","aman"]]
# nameList=["ram",{"name":"Aman"}]
# print(nameList)
# nameList=list(["aman","ram",("hello")])
# nameList=list({"aman","ram",("hello")})
# nameList=list(("aman","ram",("hello")))
# nameList=list({"name":"Aman","greet":"hello"})
# nameList=list({"name":"Aman","greet":"hello"}.values())
# print(nameList)



# fruits=("Mango",["banana","Mango"])
# fruits=("Mango",{"banana","Mango"})
# fruits=("Mango",("banana","Mango"))
# fruits=("Mango",{"name":"Apple"})
# print(fruits)
# fruits=tuple(["mango","banana"])
# fruits=tuple(("mango","banana"))
# fruits=tuple({"mango","banana"})
# fruits=tuple({"fruit":"banana"})
# fruits=tuple({"fruit":"banana"}.values())
# print(fruits)

# nameSet={"aman",{"anuj","shubham"}}  #unhashable
# nameSet={"aman",["anuj","shubham"]}  #unhashable
# nameSet={"aman",{"name":"shubham"}}    #unhashable
# nameSet={"aman",("anuj","shubham")}
# print(nameSet)

# nameSet=set(["mango","banana"])
# nameSet=set(("mango","banana"))
# nameSet=set({"mango","banana"})
# nameSet=set({"fruit":"banana"})
nameSet=set({"fruit":"banana"}.values())

print(nameSet)