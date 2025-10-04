# write a program to accept N subjects marks and print the percentage and total marks

noOfSubjects=int(input("Enter the number of subjects :")) # 7
marks=[] # list is dynamically growing array
totalMarks,percentage=0,0.0

print(f"Enter the marks of {noOfSubjects} subjects :")

for i in range(noOfSubjects): # i=0,1,2,3,4,5,6
    m=int(input(f"Enter the marks of subject {i+1} :")) # 45,67,89,90,56,78,88
    marks.append(m) # marks=[45,67,89,90,56,78,88]
    totalMarks=totalMarks+m # totalMarks=0+45=45, 45+67=112, 112+89=201, 201+90=291, 291+56=347, 347+78=425, 425+88=513 

percentage=(totalMarks/(noOfSubjects*100))*100 # (513/700)*100=73.28
print("The total marks is :",totalMarks)
print("The percentage is :",percentage)
print("The marks are :",marks)

# Advantages of List
# 1. List is mutable i.e we can change the data in list
# 2. List is ordered collection of data i.e data is stored in sequence
# 3. List can store duplicate data
# 4. List can store heterogeneous data i.e different types of data(objects)
# 5. List can grow dynamically i.e we can add,remove data at runtime
# 6. List supports indexing and slicing
# 7. List supports various inbuilt functions and methods to perform operations on list'
# 8. List can be nested i.e list can contain another list as an element



country=["india","America","Australia"]
states=[ # nested list can be created at N Dimensions 
    ["Delhi","UP","MP","HR"],
    ["Newyork","California","Texas"],
    ["South Wales","Victoria"]
]

print(country[0])
print(states[0][0])

