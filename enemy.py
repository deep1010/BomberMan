from person import *
from random import *


def move_enemy(e, arr):
    # Function for randomly moving the enemy
    import random
    for i in range(len(e)):
        chck, notry = 0, 0
        # The below lying code is for getting another random direction
        # for movement of enemy when current direction is blocked
        # when none of the direction is available the loop will terminate
        while chck != 1 and notry != 4:

            if e[i].drctn == 0:
                chck = e[i].movel(arr)
                if(chck != 1):
                    e[i].drctn = random.choice([1, 2, 3])
                    notry += 1

            elif e[i].drctn == 1:
                chck = e[i].mover(arr)
                if(chck != 1):
                    e[i].drctn = random.choice([0, 2, 3])
                    notry += 1

            elif e[i].drctn == 2:
                chck = e[i].moveu(arr)
                if(chck != 1):
                    e[i].drctn = random.choice([1, 0, 3])
                    notry += 1

            elif e[i].drctn == 3:
                chck = e[i].moved(arr)
                if(chck != 1):
                    e[i].drctn = random.choice([1, 2, 0])
                    notry += 1


def start_enemy(arr, e, count):
    # create no of enemies equal to count
    while count > 0:

        # Will generate enemies in different directions one after the other.

        x, y = 2, 4
        while(arr[x][y] != ' '):
            x = 2 * randint(10, 20)
            y = 4 * randint(10, 20)
        e.append(create_enemy(x, y, arr, 0))
        count -= 1
        if count == 0:
            break

        while(arr[x][y] != ' '):
            x = 2 * randint(10, 20)
            y = 4 * randint(1, 11)
        e.append(create_enemy(x, y, arr, 1))
        count -= 1
        if count == 0:
            break

        while(arr[x][y] != ' '):
            x = 2 * randint(1, 11)
            y = 4 * randint(10, 20)
        e.append(create_enemy(x, y, arr, 2))
        count -= 1
        if count == 0:
            break

        while(arr[x][y] != ' '):
            x = 2 * randint(1, 11)
            y = 4 * randint(1, 11)
        e.append(create_enemy(x, y, arr, 3))
        count -= 1
        if count == 0:
            break
    # At the end an array of classes of enemies will be returned.
    return e


def create_enemy(x, y, arr, drctn):
    # Will create a enemy class and return it to start_enemy function.
    temp = Enemy(x, y, arr, drctn)
    return temp


class Enemy(Person):

    def __init__(self, x, y, arr, drctn):
        Person.__init__(self, x, y, 'E')
        self.drctn = drctn
        for i in range(2):
            for j in range(4):
                arr[x + i][y + j] = 'E'
