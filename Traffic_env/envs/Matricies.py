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
        self.matrix = np.full((self.xLen,self.yLen), Tile.NAN)

        for i in range(self.yLen):
            for j in range(int(self.xLen/2-self.lanes/2), int(self.xLen/2+self.lanes/2)):
                self.matrix[i,j] = Tile.ROAD

        for i in range(self.xLen):
            for j in range(int(self.yLen/2-self.lanes/2), int(self.yLen/2+self.lanes/2)):
                self.matrix[j,i] = Tile.ROAD

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

    return x,y
