#list is mutable and ordered collection of data(objects)

# fruits=[]
# # fruits=list()
# fruits=["Apple","strawberry",67,True,"mango",45.89,"Apple"]
# basket=["Apple","strawberry","mango","Apple","banana","banana2","Banana","chiku","pineapple"]
# numbers=[10,56,75,2,45,23]
# print(fruits)
# print(basket)
# print(numbers)

# print("the fruits are :")
# for i in fruits:
#     print(i)

# marks=[1]
# marks.append(55)
# marks=marks+[67,89,89]
# print(marks)

# print(fruits[0])
# print(fruits[4])
# print(fruits[1])
# print(fruits[-2])
# length=len(fruits)
# print(length)
# print("Apple" in fruits)
# print("mango" not in fruits)

# print(fruits.index("mango"))
# fruits.append("cherry")
# print(fruits)
# print(fruits.count("Apple"))
# fruits.sort() #error bcz similar data is required for sorting
# print(fruits)

# basket.sort()
# print(basket)
# numbers.sort()
# print(numbers)
# print(fruits.pop())
# # fruits.pop()
# print(fruits)
# fruits.remove(67)
# # fruits.extend(["banana","chiku"])
# fruits.reverse()
# print(fruits)
# fruits.insert(2,"papaya")
# fruits.clear()
# fruits[2]="papaya 2.0" # if u insert this in 2nd position in empty list then it will generate error
# fruits.clear()
# print(fruits)


# Q.1 take marks from user and find percentage 

# total=0
# marks=[]
# sub=int(input("Enter subjects \n"))
# for i in range(sub):
#     marks.append(float(input("enter ur marks :")))
#     total=total+marks[i]

# print(marks)
# print("total is ",total)
# print("PERCENTAGE is ",total/sub," %")

fruits=["Apple","strawberry",67,True,"mango",45.89,"Apple"]
for f in fruits:
    # print(" the fruit is :",f)
    if isinstance(f,str):
        print(" the fruit is :",f)
    if isinstance(f,int):
        print("the number is :",f)
    if isinstance(f,float):
        print("the float is :",f)
    if isinstance(f,bool):
        print("the boolean is :",f)
