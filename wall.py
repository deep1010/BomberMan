class Wall():

    def build(self, arr):
        # A function for making the  outer and inner portions of unbreakable
        # wall
        for i in range(42):
            for j in range(84):
                if i < 2 or i >= 40:
                    arr[i][j] = 'X'
                elif j < 4 or j >= 80:
                    arr[i][j] = 'X'
                elif (i % 4 < 2) and (j % 8 in range(4)):
                    arr[i][j] = 'X'
