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

    def getBordering(self,loc,dir):
        x = int(loc[0] + dir[0])
        y = int(loc[1] + dir[1])


        if (x < 0 or x >= self.xLen) or (y < 0 or y >= self.yLen):
            return 0

        print(self.matrix[x,y])
        return self.matrix[x,y]


    def getNeighbors(self,l: []):
        x = int(l[0])
        y = int(l[1])
        n = []

        if(x < 0 and x >= self.xLen) or (y < 0 and y >= self.yLen):
            return []

        #print(x,y)

        if x > 0 and self.matrix[x-1,y] == 1:
            n += ((x-1,y))
        if x < self.xLen-1 and self.matrix[x+1,y] == 1:
            n+= ((x+1,y))
        if y > 0 and self.matrix[x,y-1] == 1:
            n+=((x,y-1))
        if y < self.yLen-1 and self.matrix[x,y+1] == 1:
            n+=((x,y+1))

        print(n)
        return n

    #Blank function for reward calculation assistance
    def getCars(self):
        return




    #Return the spaces r distance from the intersection (into intersection only)
    def GetCarsWithinRange(self,r :int = 2):
        NS = []
        WE = []
        low = self.inter_bound[0]
        high = self.inter_bound[1]

        for i in range(1,r+1):
            NS.append(self.matrix[low - i, low])
            NS.append(self.matrix[high + i, high])

            WE.append(self.matrix[high, low - i])
            WE.append(self.matrix[low, high + i])



        return NS+WE



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


