import StudentDaoImpl as dao
import os
import Student as stu

dblib=dao.StudentDaoImpl()

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
        dblib.showAllStudents()
    elif choice==2:
        alldata=dblib.showAllStudents()
    elif choice==3:
        id=int(input("enter ur id:"))
        name=input("enter ur name:")
        phone=int(input("enter ur phone no:"))
        fees=float(input("enter ur fees:"))
        isMarried=bool(input("are you married ?:"))
        address=input("enter ur address:")
        student=stu.Student(id,name,phone,fees,isMarried,address)
        dblib.addStudent(student)
    elif choice==4:
        id=int(input("enter ur id:"))
        name=input("enter ur name:")
        phone=int(input("enter ur phone no:"))
        fees=float(input("enter ur fees:"))
        isMarried=bool(input("are you married ?:"))
        address=input("enter ur address:")
        student=stu.Student(id,name,phone,fees,isMarried,address)
        dblib.updateStudent(student)
    elif choice==5:
        id2=int(input("Enter Student's id to be deleted :"))
        dblib.deleteStudent(id2)
    elif choice==6:
        exit(0)

    input("Press Any key to continue....")
