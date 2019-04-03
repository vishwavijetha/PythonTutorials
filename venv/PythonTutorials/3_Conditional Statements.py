"""
================================================================================================================================
Author: Vishwa
Date Created: 31/03/2019
--------------------------
Topic: Conditional Statements
--------------------------

Built-in: {if, elif, else}

Dictionary Implementation: {switch = {'key':'value'})
================================================================================================================================
"""

x = 10
y = 20
print("\nBuilt-in: if elif else: \n")
print('x = ', x, ',', 'y = ', y)
print('-------------------------')
if x < y:
    print('Executed for \'if x < y:\': ', x < y)
print('Outside of if statement')
print('\n')

x = True
print('x = ', x, ',', 'y = ', y)
print('-------------------------')
if x:
    print('Executed for \'if x:\'', x)

print('\n')
x = '\'Nested if elif else\''
print('x = ', x)
print('-------------------------')
if 'if' in x:
    print('if \'if\' in x: ', True)
if 'elif' in x:
    print('if \'elif\' in x: ', True)
if 'else' in x:
    print('if \'else\' in x: ', True)
elif 'Nested' in x:
    print('elif: ', True)
else:
    print('else: ', True)

# Switch implementation using Dictionary

switch = {0: 'zero', 1: 'one', 2: 'two'}
print('\n\nSwitch Implementation using Dictionary')
print('switch = ', switch)
print('-------------------------')
print('Switch[0]: ', switch[0])
print('Switch[1]: ', switch[1])
print('Switch[2]: ', switch[2])
