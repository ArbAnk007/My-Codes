#Pig is a multiplayer game (here 2 players) in which each player roll a dice and the number on dice adds up to be the score but if the players get 1 on dice the score becomes zero. The first player to get the winning scores win.

import random
import time

player1 = "Player 1"
player2 = "Player 2"

p1 = input("Enter Player 1 name (Press enter for default name): ")
p2 = input("Enter Player 2 name (Press enter for default name): ")

if p1 != '':
    player1 = p1

if p2 != '':
    player2 = p2

start = random.randint(0,1)

if start == 0:
    print("Player 1 will start first.")

else:
    print("Player 2 will start first.")

def roll_dice():
    num = random.randint(1,6)
    return num

choice = input("Ready to play! (Yes/No)")

if choice.upper() == 'YES':
    game = True
elif choice.upper() == 'NO':
    game = False
else:
    print("Invalid choice!")


break_out_flag = False
score_p1 = 0
score_p2 = 0
while score_p1 or score_p2 < 50:
    while game is True:
        if start == 0:

            print(player1, 'turn:')

            action = input("Want to Roll or Pass: ")

            if action.upper() == 'ROLL':
                score = roll_dice()

                if score != 1:
                    time.sleep(2)
                    score_p1 += score
                    print('Score of', player1, 'is:', score_p1)
                    cont = input('Wanna Roll or Pass or Quit: ')
                    if cont.upper() == 'ROLL':
                        continue
                    elif cont.upper() == 'PASS':
                        start = 1
                        continue
                    elif cont.upper() == 'QUIT':
                        game = False
                        print(player1, 'left the game!')
                        break_out_flag = True
                else:
                    time.sleep(2)
                    score_p1 = 0
                    start = 1
                    continue

        elif start == 1:

            print(player2, 'turn:')

            action = input("Want to Roll or Pass: ")

            if action.upper() == 'ROLL':
                score = roll_dice()

                if score != 1:
                    time.sleep(2)
                    score_p2 += score
                    print('Score of', player2, 'is:', score_p2)
                    cont = input('Wanna Roll or Pass or Quit: ')
                    if cont.upper() == 'ROLL':
                        continue
                    elif cont.upper() == 'PASS':
                        start = 0
                        continue
                    elif cont.upper() == 'QUIT':
                        game = False
                        print(player2, 'left the game!')
                        break_out_flag = True
                else:
                    time.sleep(2)
                    score_p2 = 0
                    start = 0
                    continue

    if break_out_flag:
        break

if score_p1 >= 50:
    print(player1, 'won the game!')
elif score_p2 >= 50:
    print(player2, 'won the game!')
else:
    print('No one won the game!')