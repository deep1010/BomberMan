class Person:

    def __init__(self, x, y, smbl):
        self.x = x
        self.y = y
        self.smbl = smbl
    # Function for moving bomberMan or Enemy

    def moveu(self, arr):
        x = self.x
        y = self.y

        # If it hits BomberMan or Enemy reduce the life

        if(arr[x - 2][y] == 'E' or arr[x - 2][y] == 'B'):
            return -1

        # Check For Feasibility of movement

        elif(arr[x - 2][y] != ' '):
            return 0

        # If possible move in corresponding direction

        else:
            self.x -= 2
            for i in range(2):
                for j in range(4):
                    arr[x + i][y + j] = ' '
                    arr[x - 2 + i][y + j] = self.smbl
            return 1

    def moved(self, arr):
        x = self.x
        y = self.y

    # If it hits BomberMan or Enemy reduce the life

        if(arr[x + 2][y] == 'E' or arr[x + 2][y] == 'B'):
            return -1

    # Check For Feasibility of movement

        elif(arr[x + 2][y] != ' '):
            return 0

    # If possible move in corresponding direction

        else:
            self.x += 2
            for i in range(2):
                for j in range(4):
                    arr[x + i][y + j] = ' '
                    arr[x + 2 + i][y + j] = self.smbl
            return 1

    def movel(self, arr):
        x = self.x
        y = self.y

    # If it hits BomberMan or Enemy reduce the life

        if(arr[x][y - 4] == 'E' or arr[x][y - 4] == 'B'):
            return -1

    # Check For Feasibility of movement

        elif(arr[x][y - 4] != ' '):
            return 0

    # If possible move in corresponding direction

        else:
            self.y -= 4
            for i in range(2):
                for j in range(4):
                    arr[x + i][y + j] = ' '
                    arr[x + i][y - 4 + j] = self.smbl
            return 1

    def mover(self, arr):
        x = self.x
        y = self.y

    # If it hits BomberMan or Enemy reduce the life

        if(arr[x][y + 4] == 'E' or arr[x][y + 4] == 'B'):
            return -1

    # Check For Feasibility of movement

        elif(arr[x][y + 4] != ' '):
            return 0

    # If possible move in corresponding direction

        else:
            self.y += 4
            for i in range(2):
                for j in range(4):
                    arr[x + i][y + j] = ' '
                    arr[x + i][y + 4 + j] = self.smbl
            return 1
