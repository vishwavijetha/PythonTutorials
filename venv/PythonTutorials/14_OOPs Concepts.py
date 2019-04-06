"""
================================================================================================================================
Author: Vishwa
Date Created: 02/04/2019
--------------------------
Topic: OOPs --> { Encapsulation, Inheritance, Abstraction, Polymorphism}
--------------------------
def: --> { self used to refer the object.  Ex: ClassName.method(classObj) == classObj.method(self gets called)}

Generic: { Instance variables(self), Class variables(cls), Instance methods, Class methods, Static methods}

Methods: { __init__(), }

================================================================================================================================
"""


class Computer:

    os = 'Windows'  # Class variable

    def __init__(self, cpu, ram):
        self.cpu = cpu  # Instance variable
        self.ram = ram

    def config(self):
        print('Config is ', self.cpu, self.ram, self.os)


comp1 = Computer('i5', '8')
comp2 = Computer('i7', '16')
comp2.os = 'MAC'

comp1.config()
comp2.config()


class Student:

    school = 'MVJ'

    def __init__(self, m1, m2, m3):
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def avg(self):
        return (self.marks1 + self.marks2 + self.marks3)/3

    @classmethod
    def get_school_name(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is a static method of School')


s1 = Student(35, 45, 55)
s2 = Student(45, 55, 65)

print(s1.avg())
print(s2.avg())
print(Student.get_school_name())
Student.info()


class Student2:

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name
        self.lap = self.Laptop()

    def show(self):
        print(self.rollno, self.name)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student2(100, 'Vishwa')
s1.show()
s2 = s1.Laptop()
s2.show()


class InheritanceA:

    def function1(self):
        print('function1() called')

    def function2(self):
        print('function2() called')


class InheritanceB(InheritanceA):

    def function3(self):
        print('function3() called')

    def function4(self):
        print('function4() called')


class InheritanceC(InheritanceB):

    def function5(self):
        print('function5() called')


a = InheritanceA()
a.function1()
a.function2()

b = InheritanceB()
b.function1()
b.function2()
b.function3()
b.function4()

c = InheritanceC()
c.function1()
c.function3()
c.function5()


class A:

    def f1(self):
        print('f1() called')


class B:

    def f2(self):
        print('f2() called')


class C(A, B):

    def f3(self):
        print('f1() called')


c = C()
c.f1()
c.f2()
c.f3()


