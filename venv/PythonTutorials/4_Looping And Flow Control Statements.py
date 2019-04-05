"""
================================================================================================================================
Author: Vishwa
Date Created: 01/04/2019
--------------------------
Topic: Looping Statements
--------------------------

Loops: {for, while} --> for i in range()/'abc', while condition

Keywords: {in, not in, range(), break, pass, continue}
================================================================================================================================
"""

print('\n\nLooping Statements:\n')
print('\'for\' loop: ')
print('-------------------------')
print('Looping through strings\n')

x = 'Python'
print('x = ', x, ',', 'len(x) = ', len(x))
print('\nfor i in x: Example\n')
for i in x:
    print(i)
print('\nfor i in range(len(x): Example\n')
for i in range(len(x)):
    print(x[i])

print('Looping through integers\n')
x = 6
print('x = ', x, ',', 'type(x) = ', type(x))
print('\nfor i in range(x): Example\n')
for i in range(x):
    print(i)
print('\nfor i in range(start,end): Example\n')
for i in range(0, 4):
    print(i)
print('\n')
for i in range(0, 10, 2):
    print('i: ', i)
print('\n')
for i in range(10, -1, -2):
    print('i: ', i)

print('\nfor i in range(5): Print multiple times: Example\n')
for i in range(5):
    print('Print for range(', i, ')',)


print('\n\n\'while\' loop:')
print('-------------------------')
i = 0
while i < 10:
    if i == 7:
        break
    elif i == 5:
        pass  # continue
    else:
        pass
    print(i)
    i += 1

print('Comprehensions')
nums = [1, 2, 3, 4]
x = [i*2 for i in nums]
print(x)


