# tup=()  #creating empty tuple
# tup=tuple()  #creating empty tuple
#tuple means row but in python tuple is a type of collection
#which is immutable and ordered and it can also store the duplicate elements

# row1=("anushka","abhishek","aman",10,56.78,"aman")

# print(row1)
# print(row1[2])
# row1[0]="anushka sharma"   # tuples are immutable
# print(row1.count("aman"))
# print(row1)
# print(row1.index("aman"))
# print(row1.index("aman",3))

# n2=("sumit 2.0","jatin 2.0")
# names=("aman","jatin","anushka","sumit")

# print(len(names))
# print(n2+names)
# print("============================")
# print(n2)
# print(names)

# tup3=n2+names
# print(tup3)
# print(type(tup3))

n2=("sumit 2.0","jatin 2.0")
l1=["hemant","raghav"]
# tup4=n2+l1  # error 
# tup4=(n2,l1)
# tup4=(n2,tuple(l1))
tup4=(n2+tuple(l1))

print(tup4)


# for e in tup4:
#     print(e,end=" |  ")

print()
for i in range(len(tup4)):
    print(" at tup[",i,"] =",tup4[i])