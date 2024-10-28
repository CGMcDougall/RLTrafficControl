import numpy as np
import pygame as pg
from enum import Enum

##Possible "tiles" (locations) that the env can have
class Tile(Enum):
    ROAD = 0
    CAR = 1
    NAN = 2

class storage:
    #init storage matrices to track locations of cars with 0,1 values 
    def __init__(self,width,height, Size = 50, Lanes = 2):
        self.lanes = Lanes

        self.width = width
        self.height = height

        self.offsetX = 20
        self.offsetY = 20

        # Sets the scaling size of matrix -> (size of screen / size = # of rows/cols)
        self.size = Size
        
        # Initialize as empty tiles, and then fill out the roads with the correct number of lanes
        self.xLen = (int(width/self.size))
        self.yLen = int(height/self.size)
        self.matrix = np.full((self.xLen,self.yLen), 2)

        self.IBX = (int(self.xLen/2-self.lanes/2), int(self.xLen/2+self.lanes/2)) #Interection Bounds X
        self.IBY = (int(self.yLen/2-self.lanes/2), int(self.yLen/2+self.lanes/2)) #Interesction Bounds Y


        for i in range(self.yLen):
            for j in range(int(self.xLen/2-self.lanes/2), int(self.xLen/2+self.lanes/2)):
                self.matrix[i,j] = 0

        for i in range(self.xLen):
            for j in range(int(self.yLen/2-self.lanes/2), int(self.yLen/2+self.lanes/2)):
                self.matrix[j,i] = 0

    #Does x,y have neighbors???? -->>> returns array max[4] min[0] of the neighbors
    def getNeighbors(self,l: [] ):
        x = l[0]
        y = l[1]
        n = []

        if(x < 0 and x >= self.xLen and y < 0 and y >= self.yLen):
            return

        if x > 0:
            n.append(self.matrix[x-1][y])
        if x < self.xLen:
            n.append(self.matrix[x + 1][y])
        if y > 0:
            n.append(self.matrix[x][y-1])
        if y < self.yLen:
            n.append(self.matrix[x][y+1])

        return n

# Potentially useful helper functions - modify and delete as appropriate
def indexToCord(self,i,j):
    x = i * (self.width / self.xLen) + self.offsetX
    y = j * (self.height / self.yLen) + self.offsetY
    return (x,y)

def getAt(self,x,y):
    x = x - self.offsetX
    x = x * (self.xLen/self.width)

    y = y - self.offsetY
    y = y * (self.yLen/self.height)

    return [int(x),int(y)]


