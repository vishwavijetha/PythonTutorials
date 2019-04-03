"""
================================================================================================================================
Author: Vishwa
Date Created: 02/04/2019
--------------------------
Topic: Functions --
--------------------------

Declaration: { def function_name()}

Methods:

Generic: {main() -- default method}
================================================================================================================================
"""
# Function definitions
print('\n\n')


def function1():
    print('function1() called', end=' --> ')


def function2(name):
    print('function2(name) called: Name = ', name, end=' --> ')


def function3(x, y):
    z = x + y
    print('function3(x, y) called: x + y = ', z, end=' --> ')
    return z


global_variable = 'Welcome to Python tutorials! '


def function4(name):
    global global_var_in_def
    global_var_in_def = 'Global value defined inside def using global keyword'
    print('function4(name) called: ', global_variable + name, end=' --> ')
    return global_variable + name


def function5():
    print('function5() called: Accessing global value defined in another def: ', global_var_in_def, end=' --> ')


# Function calls
print(type(function1()))
print(type(function2('Vishwa')))
print(type(function3(10, 20)))
print(type(function4('JARVIS')))
print(type(function5()))

