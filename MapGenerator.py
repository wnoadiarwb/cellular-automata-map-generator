import numpy as N
from numpy import int32, uint8, uint
import random
random.seed()

# Parameters
# 1) Width
# 2) Height
# 3) background color (floor/land color)
# 4) foreground color (wall/ocean color)
# 5) fill percent

class GenerateMap():
    def __init__(self, width=80,height=60, bColor=(255, 255, 255), fColor=(0, 0, 0),
                 fillPercent=50):
        self.width = width
        self.height = height
        # background and foreground color
        self.bColor = bColor
        self.fColor = fColor
        # initialize map
        self.map = N.zeros((width, height, 3), int32)
        # self.map[:] = self.bColor

        self.fillPercent = fillPercent

    def generate(self):
        self.randomFill()
        for i in range(5):
            self.smoothMap()
        return self.map

    def randomFill(self):
        for i in range(self.width):
            for j in range(self.height):
                if i == 0 or i == self.width-1 or j == 0 or j == self.height-1:
                    self.map[i][j] = self.fColor
                else:
                    if random.randint(0,100) < self.fillPercent:
                        self.map[i][j] = self.bColor
                    else:
                        self.map[i][j] = self.fColor

    def smoothMap(self):
        for i in range(self.width):
            for j in range(self.height):
                neighborWall = self.getWallCount(i,j)
                if neighborWall > 4:
                    self.map[i][j] = self.fColor
                if neighborWall < 4:
                    self.map[i][j] = self.bColor

    def getWallCount(self, gridX, gridY):
        wallCount = 0
        a = gridX - 1
        b = gridY - 1
        for i in range(a,gridX+2):
            for j in range(b,gridY+2):
                if i >= 0 and i < self.width and j >= 0 and j < self.height:
                    if i != gridX or j != gridY:
                        if (self.map[i][j] == self.fColor).all():
                            wallCount += 1
                else:
                    wallCount += 1
        return wallCount
