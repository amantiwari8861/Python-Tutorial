from abc import ABC,abstractmethod

class StudentDao(ABC):
    @abstractmethod
    def addStudent(self,Student):
        pass
    @abstractmethod
    def showAllStudents():
        pass
    @abstractmethod
    def updateStudent(self,Student):
        pass
    @abstractmethod
    def deleteStudentById(self,id):
        pass
    @abstractmethod
    def getMySQLConnection(self):
        pass