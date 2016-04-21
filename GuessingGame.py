"""
Rahul Shah
GuessingGame.py
Picks a random number to be the answer
keeps asking user for number until they get it
prints out how many times they tried to guess
"""

import random
answer = random.randrange(1,10)
again = True
trys = 1
guess = int(input("GUESS THE NUMBER, it's between 0 and 10: "))
while(guess is not answer):
    if(guess < 1 or guess > 10):
        print("Invalid number, try again")
    else:
        print("Wrong, try again")
    guess = int(input("GUESS THE NUMBER, it's between 0 and 10: "))
    trys+=1


print("YOU GOT IT, AND IT ONLY TOOK YOU ", trys, " TRIES!")
    

