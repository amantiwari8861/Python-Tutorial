import mysql.connector

# conn = pyodbc.connect(conn_str)
def getMySQLConnection():
    try:
        con=mysql.connector.connect(
        host="localhost",
        database="pdbc",
        user="root",
        password="1234"
        )
        print("Connected to MySQL successfully!")
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
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

def updateStudent(prev,id,name,phone,address,fees):
    try:
        con=getMySQLConnection()
        cursor=con.cursor()
        query="update students set id=%s,name=%s,phone=%s,address=%s,fees=%s where id=%s;"
        cursor.execute(query,(id,name,phone,address,fees,prev))
        print(cursor.rowcount," Rows updated!")
    except mysql.connector.ProgrammingError as err:
        print(err.msg)
    except Exception as e:
        print("unable to insert data in table",e)
    con.commit()
    con.close()

def deleteStudent(id2):
    try:
        con=getMySQLConnection()
        cursor=con.cursor()
        query="delete from students where id="+str(id2)+";"
        cursor.execute(query)
        if cursor.rowcount>0:
            print(cursor.rowcount," Rows Deleted!")
        else:
            print(f"{id2} doesn't exist in database!")
    except mysql.connector.ProgrammingError as err:
        print(err.msg)
    except:
        print("unable to delete data in table")
    con.commit()
    con.close()


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