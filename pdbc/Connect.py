import CRUD as dblib
import os

while True:
    os.system("cls")
    print("1.Print All students Details")
    print("2.Get All students Details")
    print("3.insert a student's Details")
    print("4.update a student's Details")
    print("5.delete a student's Details")
    print("6.exit")

    choice=int(input("Enter ur choice :"))
    if(choice==1):
        dblib.printAllStudentsData()
    elif choice==2:
        alldata=dblib.getAllStudentsData()
    elif choice==3:
        id=int(input("enter ur id:"))
        name=input("enter ur name:")
        phone=int(input("enter ur phone no:"))
        address=input("enter ur address:")
        fees=float(input("enter ur fees:"))
        dblib.insertOneRow(id,name,phone,address,fees)
    elif choice==4:
        prev=int(input("enter previous Id:"))
        id=int(input("enter ur new id:"))
        name=input("enter ur new name:")
        phone=int(input("enter ur new phone no:"))
        address=input("enter ur address:")
        fees=float(input("enter ur new fees:"))
        dblib.updateStudent(prev,id,name,phone,address,fees)
    elif choice==5:
        id2=int(input("Enter Student's id to be deleted :"))
        dblib.deleteStudent(id2)
    elif choice==6:
        exit(0)

    input("Press Any key to continue....")
