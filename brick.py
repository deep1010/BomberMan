from random import randint as ri


def check_empty(x, y, arr):
    for i in range(2):
        for j in range(4):
            if arr[x + i][y + j] != ' ':
                return -1
    return 1


class Brick:

    def create(self, arr):
        # Count will be a random number of bricks to be build
        count = ri(30, 40)

        while count > 0:
            # Generate a random multiple of 2 in range 2 <--> 38
            x = 2 * ri(1, 20)

            if x >= 8:
                y = 4 * ri(1, 20)

            else:
                y = 4 * ri(4, 20)
            # Check if the block randomly considered is available for putting a
            # brick at that position.
            temp = check_empty(x, y, arr)
            # If Yes place the brick at that position
            if temp == 1:
                for i in range(4):
                    arr[x][y + i] = "/"
                    arr[x + 1][y + i] = "/"
                count -= 1
