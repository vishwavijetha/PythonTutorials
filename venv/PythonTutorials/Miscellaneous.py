import random
# import type 1
for i in range(5):
    print(random.randint(1, 100))

print('\n')
from random import *
# import type 2
for i in range(5):
    print(randint(1, 100))

import os, sys, math
print('\n')
#print(os.system('notepad'))
print(math.fabs(-2.45))
for i in range(5):
    if i == 2:
        #sys.exit()  # Exit the program
        print()
    print(i)
print(os.path.abspath('.'))


import copy
x = [1, 2, [4, 5]]
y = copy.deepcopy(x)
print(y)
y[0] = 'New'
print(x)
print(y)

import pprint
message = 'It was a bright cold day in April, and the clocks were striking ' \
          'thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# pprint.pprint(count)
print(pprint.pformat(count))

print(chr(97))
print(chr(65))
print(ord('a'))
print(ord('A'))
print(chr(ord('y')+1))


import logging as log
log.basicConfig(filename='log.log', level=log.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
log.debug('Start of program')
log.info('hello')
log.disable(log.CRITICAL)
log.info('log is disabled')


def array_function(*data):
    print(data)


array_function('Vishwa', 30, 'a@b.com')


def dict_function(**data):
    print(data)


dict_function(name='vishwa', age=30, email='a@b.com')

fun = lambda x, y: x * y

print(fun(5,6))


def is_even(n):
    return n % 2 == 0


nums = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(is_even, nums))

print(evens)

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
