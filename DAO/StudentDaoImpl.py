import StudentDao as dao
import mysql.connector


class StudentDaoImpl(dao.StudentDao):

    def __init__(self):
        self.createTable()

    def getMySQLConnection(self):
        try:
            con = mysql.connector.connect(
                host="localhost",
                database="pdbc",
                user="root",
                password="1234")
            return con  
        except:
            print("unable to connect with mysql")

    def createTable(self):
        con=self.getMySQLConnection()
        cursor=con.cursor()
        cursor.execute("create table if not exists StudentsInfo(id int primary key auto_increment,name varchar(255),phone bigint,fees float,ismarried boolean,address varchar(255));")

    def addStudent(self, student):
        try:
            con = self.getMySQLConnection()
            cursor = con.cursor()
            query = "insert into StudentsInfo values(%s,%s,%s,%s,%s,%s);"
            data = (student.stid, student.name, student.phone, student.fees,student.isMarried,student.address)
            cursor.execute(query, data)
            print(cursor.rowcount, " Rows inserted!")
        except mysql.connector.ProgrammingError as err:
            print(err.msg)
        except:
            print("unable to insert data in table")
        con.commit()
        con.close()

    def showAllStudents(self):
        try:
            con = self.getMySQLConnection()
            cursor = con.cursor()
            cursor.execute("SELECT * FROM StudentsInfo;")
            print("\t\t\t======Student Details======")
            for i in cursor.column_names:
                print(f" %-15s " % i, end="")
            print(
                "\n------------------------------------------------------------------------------------")
            print()
            for row in cursor:
                for coldata in row:
                    print(f" %-15s " % coldata, end="")
                print()
        except:
            print("unable to select all data")

        cursor.close()

    def updateStudent(self, newStudent):
        try:
            con = self.getMySQLConnection()
            cursor = con.cursor()
            query = "update StudentsInfo set id=%s,name=%s,phone=%s,fees=%s,ismarried=%s,address=%s,where id=%s;"
            cursor.execute(query, (newStudent.stid, newStudent.name, newStudent.phone,newStudent.fees,newStudent.isMarried,newStudent.address,newStudent.stid))
            print(cursor.rowcount, " Rows updated!")
        except mysql.connector.ProgrammingError as err:
            print(err.msg)
        except:
            print("unable to insert data in table")
        con.commit()
        con.close()

    def deleteStudentById(self, id):
        try:
            con = self.getMySQLConnection()
            cursor = con.cursor()
            query = "delete from StudentsInfo where id="+str(id)+";"
            cursor.execute(query)
            print(cursor.rowcount, " Rows Deleted!")
        except mysql.connector.ProgrammingError as err:
            print(err.msg)
        except:
            print("unable to delete data in table")
        con.commit()
        con.close()
