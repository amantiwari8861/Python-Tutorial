noOfSubjects=int(input("Enter no. of subjects :"))

userData=dict()
total=0
for i in range(noOfSubjects):
    subject=input("Enter subject name:")
    marks=int(input("Enter marks of "+subject+" : "))
    total+=marks
    userData.update({subject:marks})

# print(userData)
print("Percentage :",total/noOfSubjects)
for subject,marks in userData.items():
    print("marks =",marks,"in",subject)
