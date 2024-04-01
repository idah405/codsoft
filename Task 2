import random

def play_again():
    return input('\n do you want to play again? (y/N)').lower()=='y'

def play():
    User_input = input("what do you choose? 'r' for rock 'p' for paper 's' for scissors : \n")
    Computer = random.choice(['r', 'p', 's'])

    if User_input == Computer:
        print("it's a tie ")
    elif win(User_input ,Computer):
        print(f"you won this time!!!")
    else:
        print(f"Ooops you lost")

    if play_again():
        return play()
    else:
        print('Thanks for playing! Goodbye!')

def win(player1, player2):
    if (player1 == 'r' and player2 == 's' or player1 == 's' and player2 == 'p' or player1 == 'p' and player2 == 'r'):
        return True

play()
