''' 
Author: Roger Severson
Date: July 7th, 2022
Project: Number guessing game (user vs. computer)

Objective..
1. The computer will generate a random number
2. The user will try to guess that number
3. The computer will "help" guide them to that number
4. The user will only have 5 tries
'''

# imports
from multiprocessing.sharedctypes import Value
import time, random

# welcome message
def welcome():
    name = input('What is your name? ')
    print(f'Welcome {name}!')
    time.sleep(3)
    print('Today we will be playing the number guessing game!\n'
    'You will have 5 tries to guess the number..hint it\'s between 1 and 50 ready?')
    time.sleep(5)
    print('\n\nGO!!!\n')

# computer generates the random number to guess
def random_number():
    num = random.randint(1, 3)
    return num

# validating users guess
def guess():
    while True:
        try:
            num = int(input('Enter a number: '))
            return num
        except ValueError:
            print('Not a number, try again\n')
            continue


def restart():
    play_again = input('Would you like to play again? y = yes, n = no\n')
    if play_again == 'Y':
        main()
    else:
        exit


            

# game play
def main():
    num_to_guess = random_number()
    turns = 5
    while turns > 0:
        num = guess()
        turns -= 1

        if num == num_to_guess:
            print(f'You won! Number was: {num_to_guess}')
            break

        elif num > num_to_guess:
            print('Guess was to high! Try again\n')
            continue

        else:
            print('Guess was to low! Try again\n')
            continue

    restart()




main()

