# Guess the number by user :
import random

def computer_guess(x):
    low = 1
    high= x
    feedback = ''
    while feedback != 'c':
        if low != high:
           guess = random.randint(low,high)
        else:
            guess = low # or high since high=low
        feedback=input(f"Is {guess} too high (H), two low (L) or correct (C)??").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low= guess + 1

    print (f"Congrats! The computer guessed you number,{guess},correctly!")


computer_guess(10)

        
