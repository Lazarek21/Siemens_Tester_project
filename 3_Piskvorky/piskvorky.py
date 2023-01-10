import numpy as np
import sys
import random

class GameClass:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols 
        self.matrix = np.zeros((rows, cols), dtype=str)

    def __str__(self):
        return self.matrix

    def checkIndex(self, row, cols):
        if row in range(0, self.rows) and col in range(0, self.cols):
            if self.matrix[row, col] == "":
                return True
        
        return False

    def AIMove(self):
        isSpace = False
        for rowsArr in self.matrix:
            for value in rowsArr:
                if value == '':
                    isSpace = True

        if not isSpace:
            print("wrong")
            return

        row = random.randint(0, self.rows-1)
        col = random.randint(0, self.cols-1)
        if (self.matrix[row, col] == ""):
            self.matrix[row, col] = "x"
        else:
            self.AIMove()         



if len(sys.argv) != 3:
    print("Invalid parameters")
    exit()

for line in sys.stdin:
    input = line.rstrip()
    match input:
        case "start":
            game = GameClass(int(sys.argv[1]), int(sys.argv[2]))
            x = game.rows//2
            y = game.cols//2
            game.matrix[x, y] = "x"
            print("{} {} - the AI's move".format(x, y))
        case "exit":
            exit()
        case _:
            if 'game' in locals():
                enteredValues = input.rsplit(" ")
                if len(enteredValues) == 2:
                    row = int(enteredValues[0])
                    col = int(enteredValues[1])
                    if game.checkIndex(row, col):
                        game.matrix[row, col] = "o"
                        game.AIMove()
                    else:
                        print("wrong")
                else:
                    print("wrong")
            else:
                print("wrong")
        