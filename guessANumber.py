from multiprocessing.dummy import JoinableQueue
import random

print('Hello,  what is your name? ')
name = input()
secretNumber = random.randint(1,20)
print('well, '+ name + ' I am thinking of a number between 1 and 20')

for guessesTaken in range (1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print ("Your guess is too low")
    elif guess > secretNumber:
        print ("Your guess is too high")
    else:
        break

if guess == secretNumber: 
    print("Good job, " + str(guess) + " is the correct number")
else:
    print ("WRONG! the number was " + str(guess))
