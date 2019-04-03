"""
================================================================================================================================
Author: Vishwa
Date Created: 31/03/2019
--------------------------
Topic: Variables and Data Types
--------------------------

Declaration:
x = value -- {Where x is a variable and value can be -> String, Integer, Long, Float, Boolean and Complex types }
          -- Note : x can be reassigned with any of the data type values -> x = 5, x = 'String', x = True etc

Get Data types:
type(x) -- {Where type() is function and returns  -> str, int, float, bool and complex data type names}

Casting/Converting Data types:
x = 5
str(x) -- Converts from int to string
       -- Similarly we can use other types --> int, str, float, bool, complex(x,y) etc

IO Functions:
print(msg), print('','','Print each values with spaces'),
print('',end='Skipping default \n after each print statement'),
print('','','',sep='Separate each value with any delimiter instead of comma')
x = input('Prompt msg')

AddOns:
id(x) -- Memory Address/ID of a variable x
globals()['x'] -- To access global variable value
del x -- To delete a variable

Please find Examples below:-
================================================================================================================================
"""

x = 100
delimiter = '\t\t\t\t'
print('Value', delimiter, 'DataType')
print('----------------------------------------------------------------------')
print(x, delimiter, type(x))
x = str(x)
print(x, delimiter, type(x))

x = None
print(x, delimiter, type(x))

x = 100.1234
print(x, delimiter, type(x))
x = str(x)
print(x, delimiter, type(x))
x = float(x)
print(x, delimiter, type(x))

x = 10
y = 20
z = complex(x, y)
print(z, delimiter, type(z))

x = True
print(x, delimiter, type(x))
x = str(x)
print(x, delimiter, type(x))

x = 'Single quote accepted'
print(x, delimiter, type(x))
x = "Double quote accepted. \"This is escape character example\""
print(x, delimiter, type(x))


x = (1, 2, 3, 4)
print(x, delimiter, type(x))
x = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print(x, delimiter, type(x))


print('This an example of escaping special characters by using R or r: ', R'C:\Users\vishwa.vijetha\Downloads')

a = 10
b = 10
print('a = ', a, 'b = ', b, 'Are a & b variable pointing the same memory location for integers: ', a is b)
a = "Hello"
b = "Hello"
print('Are a & b variable pointing the same memory location for strings: ', a is b)
print('Address of a: ', id(a))
print('Address of b: ', id(b))

del x

# global keyword to define global variable is optional

name = 'Vishwa'
email = 'vishwa@abc.com'
print(globals()['name'])
print(globals()['email'])

x = input('Please enter your input here: ')
print('Your input is: ', x)
