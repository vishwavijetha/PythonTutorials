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

