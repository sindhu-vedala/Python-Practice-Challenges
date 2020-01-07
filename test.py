'''
Accept input - calc the year where they turn 100
Add on - accept num and loop print
'''

NAME = input('Hey! What is your name? ')
AGE = int(input('How old are you?'))
RN = int(input('Enter a random number: '))
CURRENT_YEAR = 2019
RES = CURRENT_YEAR + (100 - AGE)
for i in range(1, RN):
    print('Hi '+NAME+'! yu will turn 100 by '+str(RES))
