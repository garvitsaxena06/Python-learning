#class and object
#importing a class from pre-exist hello.py file

class employee:
    def __init__(self, name, desig, salary):
        self.name = name
        self.desig = desig
        self.salary = salary

import hello
from hello import *

empName = input("Enter employee name: ")
empDesig = input("Enter employee designation: ")
empSalary = input("Enter employee salary: ")
obj = employee(empName, empDesig, empSalary)
print(obj.name)
