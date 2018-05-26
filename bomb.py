import os


def printwall(m, life, score, level):
    # Function for printing the board in colorful manner
    for i in range(42):

        for j in range(84):

            if m[i][j] == 'B':
                print("\033[1;32;48m" + m[i][
                      j] + "\033[0m", end='')  # Green Color

            elif m[i][j] == 'E':
                print("\033[1;31;48m" + m[i][
                      j] + "\033[0m", end='')  # Red Color

            elif m[i][j] == 'e':
                print("\033[1;33;48m" + m[i][
                      j] + "\033[0m", end='')  # Yellow/Orange Color

            elif m[i][j] == 'X':
                print("\033[0;30;40m" + m[i][
                      j] + "\033[0m", end='')  # Grey Colored Block

            elif m[i][j] == 2 or m[i][j] == 1 or m[i][j] == 0:
                print("\033[1;36;48m" + str(m[i][
                      j]) + "\033[0m", end='')  # Blue Color

            elif m[i][j] == '/':
                print("\033[0;37;47m" + m[i][
                      j] + "\033[0m", end='')  # White Colored Block

            else:
                print(m[i][j], end='')

        print('')

    print("Lives Remaining: " + str(life))
    print("Current Score: " + str(score))
    print("Current Level: " + str(level))


class Bomb:
    # Plant a bomb and update the corresponding position in the board

    def plant(self, x, y, arr):
        self.x = x
        self.y = y
        for i in range(2):
            for j in range(4):
                arr[x + i][y + j] = 2
        return
    # Function for time-clicking of bomb 2-> 1-> 0 BLAST

    def timeclick(self, arr):
        x = self.x
        y = self.y
        for i in range(2):
            for j in range(4):
                arr[x + i][y + j] -= 1

    def blast(self, arr, life, score, e, level):
        # Function For Blasting The Bomb

        x = self.x
        y = self.y

        # If BomberMan is present in the radius of blast ,reduce his life and
        # respawn him.

        if(arr[x - 1][y] == 'B' or arr[x + 2][y] == 'B' or
           arr[x][y + 4] == 'B' or arr[x][y - 1] == 'B'):
            temp = -1

        else:
            # Else clear the corresponding blast area and update the score of
            # BomberMan
            temp = 0
        p = [0, 0, 0, 0, 0]
        count1, count2 = 0, 0
        ex = [x - 1, x + 2, x, x, x]
        ey = [y, y, y + 4, y - 4, y]
        for i in range(2):
            for j in range(4):
                # Check if brick is present in blast area
                if arr[x - 1 - i][y + j] == '/':
                    count1 += 1
                if arr[x + 2 + i][y + j] == '/':
                    count1 += 1
                if arr[x + i][y + j + 4] == '/':
                    count1 += 1
                if arr[x + i][y - 1 - j] == '/':
                    count1 += 1

            # Check if Enemy is present  in blast area
                if arr[x - 1 - i][y + j] == 'E':
                    count2 += 1
                    p[0] = 1

                if arr[x + 2 + i][y + j] == 'E':
                    count2 += 1
                    p[1] = 1

                if arr[x + i][y + j + 4] == 'E':
                    count2 += 1
                    p[2] = 1

                if arr[x + i][y - 1 - j] == 'E':
                    count2 += 1
                    p[3] = 1
                if arr[x + i][y + j] == 'E':
                    p[4] = 1
            # Animate Blast area

                if arr[x - 1 - i][y + j] != 'X':
                    arr[x - 1 - i][y + j] = 'e'
                if arr[x + 2 + i][y + j] != 'X':
                    arr[x + 2 + i][y + j] = 'e'
                if arr[x + i][y - 1 - j] != 'X':
                    arr[x + i][y - 1 - j] = 'e'
                if arr[x + i][y + 4 + j] != 'X':
                    arr[x + i][y + j + 4] = 'e'
                arr[x + i][y + j] = 'e'
            # If Enemy was present then delete the corresponding class of enemy
            # and update the board
                todel = []
                for a in range(5):
                    for b in range(len(e)):
                        if p[a] == 1:
                            if e[b].x == ex[a] and e[b].y == ey[a]:
                                todel.append(b)
                todel.sort()
                todel.reverse()
                for c in todel:
                    del e[c]
        # Update Score +20 for Brick and +100 for Enemy
        score += (count1 / 8) * 20 + ((count2 / 8) * 100)

        os.system('clear')

        printwall(arr, life, score, level)
        # Bring the blast area on board to normal
        for i in range(2):
            for j in range(4):
                if arr[x - 1 - i][y + j] == 'e':
                    arr[x - 1 - i][y + j] = ' '
                if arr[x + 2 + i][y + j] == 'e':
                    arr[x + 2 + i][y + j] = ' '
                if arr[x + i][y - 1 - j] == 'e':
                    arr[x + i][y - 1 - j] = ' '
                if arr[x + i][y + 4 + j] == 'e':
                    arr[x + i][y + j + 4] = ' '
                arr[x + i][y + j] = ' '
        # return status of presence of bomberman in blast area and score
        return [temp, score]
