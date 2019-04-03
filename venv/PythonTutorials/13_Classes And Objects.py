"""
================================================================================================================================
Author: Vishwa
Date Created: 03/04/2019
--------------------------
Topic: Classes And Objects --
--------------------------

Keywords: { class, @classmethod, @staticmethod}

Methods: { __init__, __del__}

Generic: {}
================================================================================================================================
"""


class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def display_count():
        print("Total Employee %d" % Employee.empCount)

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee('Vishwa', 1000)
emp2 = Employee('Vijetha', 2000)

emp1.display_employee()
emp2.display_employee()


class A:
    class_var = 'class variable'
    __name = 'Vishwa'

    def print(self):
        print(self._name)

    @staticmethod
    def function():
        print('function() called')


a = A()
print(a.class_var)
a.class_var = 'updated'
print(a.class_var)
a.function()
