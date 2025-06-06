

# ! 04/06/25
# //?------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ! WHILE LOOP:
# Three Loop Questions:
# 1. What do I want to repeat?
#  -> message
# 2. What do I want to change each time?
#  -> stars
# 3. How long should we repeat?
#  -> 5 times

import random


print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

i = 1
while i <= 5:
    print(f"{i} Loops are great*")
    i += 1


#  ! EXERCISE
print('Guessing game')
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)


num = 12
guess = 0
guess_limit=3
guess_number = 0

while guess_number < guess_limit:
    guess = int(input(f'Guess # {guess_number} a number 1-20: last guess:{guess} '))
    if guess == num:
        print(f'You Win! You Guessed it: {guess}')
        break
    else:
        print(f'No, not {guess}!')
        guess_number += 1
if guess != num:
    print(f'Sorry you lose! It was {num}')
