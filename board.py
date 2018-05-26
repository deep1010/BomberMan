import os
import getch
from wall import *
from bomberman import *
from brick import *
from Gameover import *
from enemy import *
from bomb import *
from Youwin import *
import time

planted = 0
moves = 0

# Create a 2-D Matrix For Board
Matrix = [[' ' for x in range(84)] for y in range(42)]

# Function for moving the bomberman in possible directions


def move(z):
    if z == 'a':
        return bm.movel(Matrix)

    if z == 'w':
        return bm.moveu(Matrix)

    if z == 'd':
        return bm.mover(Matrix)

    if z == 's':
        return bm.moved(Matrix)

life = 3
score = 0
level = 1
# Create the classes for Bomberman,Wall,Brick,Bomb
bm = Bomberman()
w = Wall()
br = Brick()
bomb = Bomb()

# Build the wall,brick,bomberman
w.build(Matrix)
br.create(Matrix)
bm.create(Matrix)

# Create an array of classes od enemies

etemp = []
e = start_enemy(Matrix, etemp, 3 + level)

os.system("clear")

# print the initial stage of game

printwall(Matrix, life, score, level)

ret = 0
while True:
    # Get the input from user
    z = getch.getch()
    # Lag the game by 0.1 seconds
    time.sleep(0.1)

    if z == 'q':
        # Exit the game
        os.system("clear")
        break

    if z == 'b':
        # Plant the bomb
        if planted == 0:
            # plant a bomb only if currently there are no bombs present on the
            # board
            temp = 0
            # remember the current positoin of bomberman

            old_x = bm.x
            old_y = bm.y
            # bomb will only appear when bomberman moves
            while temp != 1:
                temp = move(getch.getch())

            moves = 1
            # plant the bomb

            bomb.plant(old_x, old_y, Matrix)
            planted = 1
    # Move the BomberMan if the key-press is 'a' or 's' 'd' or 'w'
    elif z in ['a', 's', 'd', 'w']:

        ret = move(z)
    # time-ticking of bomb
        if planted == 1:
            bomb.timeclick(Matrix)

        if(ret >= 0):
            moves += 1

    os.system("clear")
    printwall(Matrix, life, score, level)

    # Explode the bomb after 3 frames and if it is planted

    if planted == 1 and moves == 3:
        [ret, score] = bomb.blast(Matrix, life, score, e, level)

        # if all the enemies are dead move on to next level

        if len(e) == 0:
            level += 1

            # When all levels are completed

            if level == 4:
                os.system("clear")
                youwin(score)
                break
            # Move on to next level-> respawn bomberman,regenerate bricks and
            # enemies

            else:
                for qw in range(2):
                    for wq in range(4):
                        Matrix[bm.x + qw][bm.y + wq] = ' '
                # delete old objects
                del e
                del etemp
                del bm
                # create new ones

                br.create(Matrix)
                bm = Bomberman()
                bm.create(Matrix)

                etemp = []
                e = start_enemy(Matrix, etemp, 3 + level)
        planted = 0

    # If bomberman hits a enemy reduce his life

    if(ret == -1):

        # Respawn the bomberman

        life -= 1
        for i in range(2):
            for j in range(4):
                Matrix[bm.x + i][bm.y + j] = ' '
        del bm
        bm = Bomberman()
        bm.create(Matrix)

        # Remove the currently placed bomb

        if(planted == 1):
            for i in range(2):
                for j in range(4):
                    Matrix[bomb.x + i][bomb.y + j] = ' '
        moves = 0
        planted = 0
        del bomb
        bomb = Bomb()

        os.system("clear")
        printwall(Matrix, life, score, level)

        # If all lives are over end the game

        if life == 0:
            gameover()
            break
    print("Enemies Left:", len(e))

    # randomize the movement of enemy

    move_enemy(e, Matrix)
