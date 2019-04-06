"""
================================================================================================================================
Author: Vishwa
Date Created: 01/04/2019
--------------------------
Topic: Dictionary -- Mutable, No duplicate keys allowed and No order maintained like List
--------------------------

Declaration: {x = {}, x = {key: value, key: value}}

Methods: 11 --> {copy(), keys(), values(), items(), get(), update(), pop(), popitem(), setdefault(), fromkeys(),clear()}

Generic: --> {min(), max(), len()}
================================================================================================================================
"""

# Declaring Lists
print('\nDeclaring a Dictionary:\n')
x = {}  # {} means it's a List type
print('1) x = {}, type(x) = ', type(x))
print(x)
x = {1: 'one', 2: 'two', 3: 'three'}
print('2) x = ', x, type(x))

print('\nAccessing values from the Dictionary:\n')
x = {1: 'one', 2: 'two', 7: 'seven', 4: 'four'}
print('x = ', x)
print('----------------------------------------------------------------------')
print('x[1]: ', x[1])
print('x[2]: ', x[2])
print('x[7]: ', x[7])
print()

print(1 in x.keys())
print('one' not in x.values())
print()

print('len(x): ', len(x))
print('max(x): ', max(x))
print('min(x): ', min(x))


print('\nDictionaries are Mutable: Example\n')
print('Before --> x = ', x)
x[1] = 'New Value for One'
print('x[1] =', '\'', x[1], '\'')
print('After --> x = ', x)

print()
print('dict({}) function example: ', dict({'a': 1, 'b': 2, 'c': 3}))

print('\nDictionary operations:\n')
print('----------------------------------------------------------------------')
print('1) Copy: Syntax --> copy()\n')
print('x = ', x)
y = x.copy()
print('y = x.copy() ', '\ny = ', y)
print()

print('2) Keys: Syntax --> keys()\n')
print('x = ', x)
print('x.keys(): ', x.keys())
print()

print('3) Values: Syntax --> values()\n')
print('x = ', x)
print('x.values(): ', x.values())
print()

print('4) Items: Syntax --> items()\n')
print('x = ', x)
print('x.items(): ', x.items())
print()

print('5) Get: Syntax --> get(key)\n')
print('x = ', x)
print('x.keys(): ', x.get(2))
print()

print('6) Update: Syntax --> update(dict2)\n')
print('x = ', x)
y = {'a': 123, 'b': 456}
print('y = ', y)
x.update(y)
print('x.update(y): ', x)
print()

print('7) Pop: Syntax --> pop(key)\n')
print('x = ', x)
x.pop(1)
print('x.pop(1) ', '\n', x)
print()

print('8) Popitem: Syntax --> popitem()\n')
print('x = ', x)
x.popitem()
print('x.popitem() ', '\n', x)
print()

print('9) SetDefault: Syntax --> setdefault(key,defaultValue)\n')
print('x = ', x)
z = x.setdefault(2, 'set as default value')
print('z = x.setdefault(2, \'default value inserted\') ', '\n', z)
print()

print('10) FromKeys: Syntax --> fromkeys(seq)\n')
keys = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys)
print('keys = ', keys)
print('vowels = dict.fromkeys(keys)', vowels)


print('11) Clear: Syntax --> clear()\n')
print('x = ', x)
x.clear()
print('x.clear()', '\n', 'x = ', x)



