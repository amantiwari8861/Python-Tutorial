import mysql.connector

# conn = pyodbc.connect(conn_str)
def getMySQLConnection():
    try:
        con=mysql.connector.connect(
        host="localhost",
        database="pdbc",
        user="root",
        password="1234" )
    except:
        print("unable to connect with mysql")

    return con

def getAllStudentsData():
    con=getMySQLConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students;")
    return cursor.fetchall()

def printAllStudentsData():
    try:
        con=getMySQLConnection()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM students;")
        print("\t\t\t======Student Details======")
        for i in cursor.column_names:
            print(f" %-15s "%i,end="")
        print("\n------------------------------------------------------------------------------------")
        print()
        for row in cursor:
            for coldata in row:
                print(f" %-15s "%coldata,end="")
            print()
    except:
        print("unable to select all data")
    
    cursor.close()

def insertOneRow(stid,name,phone,address,fees):
    try:
        con=getMySQLConnection()
        cursor=con.cursor()
        query="insert into students values(%s,%s,%s,%s,%s);"
        data=(stid,name,phone,address,fees)
        cursor.execute(query,data)
        print(cursor.rowcount," Rows inserted!")
    except:
        print("unable to insert data in table")
    con.commit()
    con.close()

print("1.Print All students Details")
print("2.Get All students Details")
print("3.insert a student's Details")

choice=int(input("Enter ur choice :"))
if(choice==1):
    printAllStudentsData()
elif choice==2:
    alldata=getAllStudentsData()
elif choice==3:
    id=int(input("enter ur id:"))
    name=input("enter ur name:")
    phone=int(input("enter ur phone no:"))
    fees=float(input("enter ur fees:"))

    insertOneRow(id,name,phone,fees)

'''
show databases;
create database pdbc;
create table Students(id int primary key,name varchar(255),phone bigint,address varchar(255),fees float);
desc students;
show tables;
insert into students values(100,"Aman",9891062743,"Niit 62 Noida",5000.56);
 --truncate students;
insert into students values 
(101,"Aman",9891062743,"Niit 62 Noida",5000.56),
(102,"Naman",9891062743,"Niit 32 Noida",800.56),
(103,"Anmol",9891062743,"Niit 67 Noida",300.56),
(104,"Jai Singh",9891062743,"Niit 98 Noida",15000.56);
select * from students where name like '%n';
'''