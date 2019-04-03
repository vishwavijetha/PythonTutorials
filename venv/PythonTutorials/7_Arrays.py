"""
================================================================================================================================
Author: Vishwa
Date Created: 01/04/2019
--------------------------
Topic: Arrays --
--------------------------

Declaration: {x = array('type code', [list])}

Methods: --> {insert(), remove(), append(), pop(), index(), extend(), sort(), count(), copy(), reverse(), clear()}

Generic: --> {min(), max(), len()}

Type Code: --> {'i', 'I', 'f', 'd', 'l', 'L', 'b', 'B', 'u', 'h', 'H'}
================================================================================================================================
"""
from array import *
# Declaring Arrays
print('\nDeclaring an Array:\n')
x = array('i', [1, 2, 3, 4])
for i in x:
    print(i)

print()
print(x.typecode)
