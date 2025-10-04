#list is mutable and ordered collection of data(objects)

# fruits=[] # creating empty list
# fruits=list() # creating empty list using constructor
# print(type(fruits))
fruits=["Apple","strawberry",67,True,"mango",45.89,"Apple"]
# print(fruits)
# basket=["Apple","strawberry","mango","Apple","banana","banana2","Banana","chiku","pineapple"]
# print(basket)
# basket[0]="Kashmiri Apple"
# print(basket)
# print(basket[3])
# print(basket[-1])
# numbers=[10,56,75,2,45,23]
# print(numbers)

# print(fruits[0])
# print(fruits[4])
# print(fruits[1])
# print(fruits[-2])

# Iterating a list using for loop
# print("the fruits are :")
# for i in fruits:
#     print("fruit :",i)

# for i in range(len(fruits)):
#     print(f"at position {i} fruit :",fruits[i])

# marks=[59]
# # marks.append(55)
# marks=marks+[67,89,36]
# print(marks)


# there are exactly 11 inbuilt functions on list
 
# len(),in,not in is not list function
# length=len(fruits) # len() function returns the length of list
# print(length)
# print("Apple" in fruits) # membership operator
# print("mango" not in fruits) # membership operator

# print(fruits.index("mango")) # returns the index of first occurrence of element
# print(fruits.index("Apple")) # returns the index of first occurrence of element
# print(fruits.index("Apple",2)) # returns the index of first occurrence of element after 2nd index
# fruits.append("cherry")
# print(fruits)
# print(fruits.count("Apple"))
# fruits.sort() #error bcz similar data is required for sorting
# print(fruits)

# basket=["Apple","strawberry","mango","Apple","banana","banana2","Banana","chiku","pineapple"]
# numbers=[10,56,75,2,45,23]
# basket.sort()
# print(basket)
# numbers.sort()
# print(numbers)
# print(fruits.pop())
# fruits.pop()
# print(fruits)
# fruits.remove(67)
# fruits.pop(0)
# print(fruits)
# fruits.extend(["banana","chiku"])
# fruits.reverse()
# fruits.insert(2,"papaya")
# print(fruits)
# fruits.clear()

# fruits[2]="papaya 2.0" # if u insert this in 2nd position in empty list then it will generate error
# fruits.append("dragon fruit")
# # # fruits.clear()
# print(fruits)


fruits=["Apple","strawberry",67,True,"mango",45.89,"Apple",None]
for f in fruits:
    # print(" the fruit is :",f)
    if isinstance(f,str):
        print(" the fruit is :",f)
    elif isinstance(f,int):
        print("the number is :",f)
    elif isinstance(f,float):
        print("the float is :",f)
    elif isinstance(f,bool):
        print("the boolean is :",f)
    else:
        print("the datatype is unknown :",f)
