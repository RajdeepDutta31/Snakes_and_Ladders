# Snakes and Ladder upto 20
import random
snakes = [9, 17, 18] # -> [2, 4, 7]
ladders = [3, 6]   # -> [12, 14]

def roll():
    dice = random.randint(1,6)
    return dice

player = 1
def play():
    global player
    print("Player is in now {}th position".format(player))
    move = roll()
    player = player + move
    print("Rolling the dice.....\nIt's",move)
    if player>20:
        player = player - move

    if player in ladders:
        print("Player is in now {}th position".format(player))
        print("Climbing a ladder.... :) ")
        if (player==3):
            player = 12
        elif (player==6):
            player = 14
        #print("Player is in now {}th position".format(player))
    
    elif player in snakes:
        print("Player is in now {}th position".format(player))
        print("Hissss..... a snake :( ")
        if (player==9):
            player = 2
        elif (player==17):
            player = 4
        elif (player==18):
            player = 7
        #print("Player is in now {}th position".format(player))

    
while(player!=20):    
        play()

print("Player is in now {}th position".format(player))
print("You Win")
