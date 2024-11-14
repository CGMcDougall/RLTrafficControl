import numpy as np
import pygame as pg
from enum import Enum

##Possible "tiles" (locations) that the env can have
class Tile(Enum):
    ROAD = 0
    CAR = 1
    INTER = 2       #Intersection
    OCC_INTER = 3   #Occupied Intersection
    NAN = 4

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
                if(self.IBY[0] <= i and self.IBY[1] > i):
                    self.matrix[i,j] = 3
                else:
                    self.matrix[i,j] = 0

        for i in range(self.xLen):
            for j in range(int(self.yLen/2-self.lanes/2), int(self.yLen/2+self.lanes/2)):
                if (self.IBX[0] <= i and self.IBX[1] > i):
                    self.matrix[i, j] = 3
                else:
                    self.matrix[j,i] = 0

    #Does x,y have neighbors???? -->>> returns array max[4] min[0] of the neighbors

    def getBordering(self,loc,dir):
        x = int(loc[0] + dir[0])
        y = int(loc[1] + dir[1])



        if (x < 0 or x >= self.xLen) or (y < 0 or y >= self.yLen):
            return 0

        print(self.matrix[y,x])
        return self.matrix[y,x]


    #Blank function for reward calculation assistance
    def getCars(self):
        return


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


 # def atLight(self):
 #        IBX = self.IBX
 #        IBY = self.IBY
 #
 #        if abs(self.dir[0]) == 1 and phase == LightAction.H_GREEN:
 #            self.driving = True
 #            return
 #        if abs(self.dir[1]) == 1 and phase == LightAction.V_GREEN:
 #            self.driving = True
 #            return
 #
 #        if self.dir[0] == 0:
 #            self.loc[1] = Matricies.getAt(mat, self.Car.x, self.Car.y)[1]
 #        else:
 #            self.loc[0] = Matricies.getAt(mat, self.Car.x, self.Car.y)[0]
