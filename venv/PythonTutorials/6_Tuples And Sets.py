"""
================================================================================================================================
Author: Vishwa
Date Created: 01/04/2019
--------------------------
Topic: Tuple Sets -- Immutable
--------------------------

Declaration: {x = (), x = (1,'Hi',2.75,None), x = (1, (1,2,3), (4,5,6), 5)}

Methods: 11 --> {index(), count()}

Generic: --> {min(), max(), len()}
================================================================================================================================
"""

# Declaring Tuples
print('\nDeclaring a Tuple Set:\n')
x = ()  # () means it's a Tuple Set type
print('1) x = (), type(x) = ', type(x))
print(x)
x = (1, 2, 'Hi', 'Hello', 1.1, 2.2, True, False, complex(1, 2), complex(2, 3))
print('2) x = (1, 2, \'Hi\', \'Hello\', 1.1, 2.2, True, False, complex(1, 2), complex(2, 3))', type(x))
print(x)
x = (1, 2, (1, 2), (3, 4), 5)
print('3) x = ', x, type(x))
print(x)

print('\nAccessing values from the Tuple:\n')
x = (1, 2, ('Hi', 'Hello'), (True, False), 1.1, 2.2, complex(1, 2), complex(3, 4))
print('x = ', x)
print('----------------------------------------------------------------------')
print('x[0]: ', x[0])
print('x[2]: ', x[2])
print('x[2][0]: ', x[2][0])
print('x[3][1]: ', x[3][1])
print('x[1:]: ', x[1:])
print('x[-1]: ', x[-1])
print('x[-2]: ', x[-2])
print('x[2:4]: ', x[2:4])
print('x[:2]: ', x[:2])
print('x[:]: ', x[:])

"""
Throws an error
print('\nTuples are Immutable: Example\n')
print('Before --> x = ', x)
x[0] = 'Value cannot be Changed'
print('x[0] =', '\'', x[0], '\'')
print('After --> x = ', x)
"""

print('\nTuple operations:\n')
x = ('a', 'b', 'c', 'd', )
print('----------------------------------------------------------------------')
print('1) Count: Syntax --> count(object/value)\n')
print('x = ', x)
print('x.count(\'a\') --> ', x.count('a'))
print('\n')

print('2) Index: Syntax --> index(object/value, startIndex, stopIndex)\n')
print('x = ', x)
print('x.index(\'a\', 3, -1) --> ', x.index('c'))
print('\n')

print('----------------------------------------------------------------------')
print()
print('Conversion from Tuple to List and vice versa')
x = (1, 2, 3)
print('x = ', type(x), x)
y = list(x)
print('y = ', type(y), y)

x = [1, 2, 3]
print('x = ', type(x), x)
y = tuple(x)
print('y = ', type(y), y)

print('len(x): ', len(x))
print('len(y): ', len(y))
print('max(x): ', max(x))
print('min(x): ', min(x))

x = {1, 2, 3, 4, 4}
print(x)






