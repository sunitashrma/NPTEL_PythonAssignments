import random

def play ():
    user=input("'What colour you want??','r' for Red, 'y'for Yellow,'g' for Green\n")
    computer=random.choice(['r','y','g'])

    if user == computer:
        return 'it is a tie.'

    # r > y , y > g, g > r

    if is_win(user,computer):
        return 'You won!'

    return 'You lost!'

def is_win (player,opponent):
    # its true if player wins
    # r > y , y > g, g > r\
    if (player == 'r' and opponent == 'y') or (player=='y' and opponent =='g') \
       or (player == 'g' and opponent =='r'):
       return True
    
print(play())
    
