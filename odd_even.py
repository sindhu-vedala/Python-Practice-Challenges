'''
Odd or even
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0 :
        print('Weird')
    else:
        if n in range(2,5):
            print('Not Weird')
        elif n in range(6,21):
            print('Weird')
        else:
            print('Not Weird')


# while True:
#     try:
#         NUM = int(input('Enter a number: '))
#         break
#     except ValueError:
#         print('YOu need to enter an integer')

# while True:
#     try:
#         CHECK = int(input('Enter a second number: '))
#         break
#     except ValueError:
#         print('YOu need to enter an integer')

# try:
#     if NUM%CHECK == 0:
#         print('Perfect')
#     else:
#         print('Naah')
# except ZeroDivisionError:
#     print('Oops cannot divide by 0!')


# if NUM%4 == 0:
#     print('Divisible by 4')
# elif NUM%2 == 0:
#     print('YOU entered an even number')
# else:
#     print('YOu entered an odd number')
