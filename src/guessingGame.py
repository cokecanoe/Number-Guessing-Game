
import random

number = random.randint(1,10)
print ("Guess a number between 1-50 \n")
guess = int(input())

win = False

while win == False: 
    if guess == number:
        print ("Congragulations! You win! \n")
        win = True
    else:
        if guess > number:
            print("Lower \n")
        else:
            print("Higher \n")
        guess = int(input())






