"""
================================================================================================================================
Author: Vishwa
Date Created: 01/04/2019
--------------------------
Topic: String Manipulations --
--------------------------

Methods: --> {join(), reversed(), upper(), lower(), startswith(), endswith(), find(), replace(), split(), isupper(),\
                islower(), isa}

Generic: --> {min(), max(), len()}
================================================================================================================================
"""

x = "Welcome to Python Tutorials!!"
print('x = ', x)
print('Length: len(x): ', len(x))
x = x + ' Have a good day!!'
print('Concatenation: x + \'Have a good day!!\' ', x)
print('String multiplication: x * 2: ', x * 2)

print('\n\nString Parsing: \n')
print('x = ', x)
print('x[0]: ', x[0])
print('x[0:4]: ', x[0:4])
print('x[3:5]: ', x[3:5])
print('x[:8]: ', x[:8])
print('x[8:]: ', x[8:])
print('x[-1]: ', x[-1])
print('x[-2]: ', x[-2])
print('x[-2]: ', x[-3])
print('x[:]: ', x[:])
print('l in x: ', 'l' in x)
print('z not in x: ', 'z' not in x)
print('Reversed String: reversed(x):', ''.join((reversed(x))))
print('UpperCase: ', x.upper())
print('LowerCase: ', x.lower())
print('Ends with day!!: ', x.endswith('day!!'))
print('Starts with Welcome: ', x.startswith('Welcome'))
print('Contains: ', 'python' in x.lower())
print('Replace good with nice: ', x.replace('good', 'nice'))
print('Split: ', x.split(' '))
print('RSplit: ', x.rsplit(' '))
print('Is AlphaNumeric: abc123: ', 'abc123'.isalnum())
print('Is UpperCase: ABC: ', 'ABC'.isupper())
print('Capitalize: hello world: ', 'hello world'.capitalize())
print('Represent String/Number format: %s %d: ' % (x[0:8], 100))
print(''' no need to use r/R or escape characters ',",) 
because this is a short cut using triple quotes''')
