class Employee:
    __id=0
    def __init__(self):
        __name="Aman"
        __salary=0

emp1=Employee()
# emp1.__id=101
# print(emp1.__id)
# print(emp1.__name) # error
# emp1.__salary=50000
# print(emp1.__salary)
print(emp1.getName())