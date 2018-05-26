from person import *
# Inherit the Person class


class Bomberman(Person):

    def __init__(self):
        Person.__init__(self, 2, 4, 'B')
    # Create the bomberman and update the board

    def create(self, arr):
        x = self.x
        y = self.y
        s = self.smbl
        for i in range(2):
            for j in range(4):
                arr[x + i][y + j] = s
