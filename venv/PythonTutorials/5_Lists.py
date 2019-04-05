"""
================================================================================================================================
Author: Vishwa
Date Created: 01/04/2019
--------------------------
Topic: Lists -- Mutable and Ordered
--------------------------

Declaration: {x = [], x = [1,'Hi',2.75,None], x = [1, [1,2,3], [4,5,6], 5]}

Methods: 11 --> {insert(), remove(), append(), pop(), index(), extend(), sort(), count(), copy(), reverse(), clear()}

Generic: --> {min(), max(), len()}
================================================================================================================================
"""
# Declaring Lists
print('\nDeclaring a List:\n')
x = []  # [] means it's a List type
print('1) x = [], type(x) = ', type(x))
print(x)
x = [1, 2, 'Hi', 'Hello', 1.1, 2.2, True, False, complex(1, 2), complex(2, 3)]
print('2) x = [1, 2, \'Hi\', \'Hello\', 1.1, 2.2, True, False, complex(1, 2), complex(2, 3)]', type(x))
print(x)
x = [1, 2, [1, 2], [3, 4], 5]
print('3) x = [1, 2, [1, 2], [3, 4], 5]', type(x))
print(x)

print('\nAccessing values from the List:\n')
x = [1, 2, ['Hi', 'Hello'], [True, False], 1.1, 2.2, complex(1, 2), complex(3, 4)]
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
print('\nLists are Mutable: Example\n')
print('Before --> x = ', x)
x[0] = 'Value Changed'
print('x[0] =', '\'', x[0], '\'')
print('After --> x = ', x)

print()
x = [3, 4, 5]
print('len(x): ', len(x))
print('max(x): ', max(x))
print('min(x): ', min(x))

print()
print(list('HELLO'))

print('\nList operations:\n')
x = ['a', 'b', 'c', 'd', ]
print('----------------------------------------------------------------------')
print('1) Insert: Syntax --> insert(index, value)\n')
print('x = ', x)
print()
x.insert(0, 1)
print('x.insert(0, 1) --> ', x)
x.insert(1, 'Hi')
print('x.insert(1, \'Hi\') --> ', x)
x.insert(2, 2.75)
print('x.insert(2, 2.75) --> ', x)
x.insert(3, None)
print('x.insert(3, None) --> ', x)
print('\n')

print('2) Remove: Syntax --> remove(object/value)\n')
print('x = ', x)
x.remove(None)
print('x.remove(None) --> ', x)
x.remove('Hi')
print('x.remove(\'Hi\') --> ', x)
print('\n')

print('3) Append: Syntax --> append(object/value)\n')
print('x = ', x)
x.append('Append1')
print('x.append(\'Append1\') --> ', x)
x.append('Append2')
print('x.append(\'Append2\') --> ', x)
print('\n')

print('4) Pop: Syntax --> pop(index)\n')
print('x = ', x)
x.pop()
print('x.pop() --> ', x)
x.pop(1)
print('x.pop(1) --> ', x)
print('\n')

print('5) Extend/Concat: Syntax --> extend(another list)\n')
print('x = ', x)
y = ['a', 'b']
x.extend(y)
print('Extended list: ', x)
print('\n')

print('6) Count: Syntax --> count(object/value)\n')
print('x = ', x)
print('x.count(\'a\') --> ', x.count('a'))
print('\n')

print('7) Index: Syntax --> index(object/value, startIndex, stopIndex)\n')
print('x = ', x)
print('x.index(\'a\', 3, -1) --> ', x.index('a', 3, -1))
print('\n')

print('8) Reverse: Syntax --> reverse()\n')
print('x = ', x)
x.reverse()
print('x.reverse() --> ', x)
print('\n')

print('9) Copy: Syntax --> copy()\n')
y = x.copy()
print('x = ', x)
print('y = ', y)
print('\n')

print('10) Sort: Syntax --> sort(key,reverse)\n')
x = ['z', 'y', 'x', 'c', 'b', 'a']
print('x = ', x)
x.sort(reverse=False)
print('x.sort() --> ', x)
print('\n')

print('11) Clear: Syntax --> clear()\n')
x = ['z', 'y', 'x', 'c', 'b', 'a']
print('x = ', x)
x.clear()
print('x.clear() --> ', x)
print('\n')

