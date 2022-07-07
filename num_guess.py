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
    num = random.randint(1, 50)
    return num

# play again?
def game_loop():
    user_input = input('\nWould you like to play again?\n y = yes and n = no: ')
    while True:
        if user_input.capitalize == 'Y':
            main()
        else:
            break
        

# main game
def main():
    num_to_guess = random_number()
    turns = 5
    while True:
        try:
            print(f'Remaining attemps: {turns}')
            guess = int(input('Enter a number: '))
            turns -= 1

            if guess == num_to_guess:
                print(f'You got the number it was {num_to_guess}')
                game_loop()
            elif turns == 0:
                print(f'You ran out of turns, the number was {num_to_guess}')
                game_loop()
            elif guess > num_to_guess:
                print('You guess was to high!\n')
                continue
            else:
                print('Guess was to low!\n')
                continue
            
        except ValueError:
            print('Not a number try again\n')

welcome()
main()
        
