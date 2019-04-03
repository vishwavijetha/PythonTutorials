"""
================================================================================================================================
Author: Vishwa
Date Created: 03/04/2019
--------------------------
Topic: Exception Handling --
--------------------------

Keywords: { try, except, else, raise, finally}

Exceptions: {Exception, StandardError, ArithmeticError, ImportError, RuntimeError etc}
Methods:

Generic: {}
================================================================================================================================
"""

try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except SyntaxError as e:
    print('Syntax Error: ', e)
except IOError as e:
    print("Error: can\'t find file or read data", e)
else:
    print("Written content in the file successfully")
finally:
    print('finally() called regardless of try/except')


def function1(level):
    if level < 1:
        raise Exception("Invalid level!", level)


function1(0)
