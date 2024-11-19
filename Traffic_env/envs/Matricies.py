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
    def __init__(self, screen_size = 700, mat_size = 14, Lanes = 2):
        self.lanes = Lanes
        self.screen_size = screen_size
        self.mat_size = mat_size
        
        # Pixel lengths
        self.pixel_len = (int(screen_size/self.mat_size))

        # Initialize as empty tiles, and then fill out the roads with the correct number of lanes
        self.matrix = np.full((self.mat_size,self.mat_size), 0)
        self.inter_bound = (int(self.mat_size/2)-1, int(self.mat_size/2))

        for i in range(self.inter_bound[0], self.inter_bound[1]+1):
            for j in range(self.inter_bound[0], self.inter_bound[1]+1):
                self.matrix[i,j] = 2

    def getBordering(self,loc,dir):
        x = int(loc[0] + dir[0])
        y = int(loc[1] + dir[1])

        if (x < 0 or x >= self.mat_size) or (y < 0 or y >= self.mat_size):
            return 0

        return self.matrix[y,x]
    def withinIntersectionBounds(self,loc) -> bool:
        x = int(loc[0])
        y = int(loc[1])
        #print(self.inter_bound[0],self.inter_bound[1])

        return (self.inter_bound[0] <= x and self.inter_bound[1] >= x and self.inter_bound[0] <= y and self.inter_bound[1] >= y)

# Helper Functions
def indexToCord(self,i,j):
    x = i * self.pixel_len
    y = j * self.pixel_len
    return (x,y)

def cordToIndex(self,i,j):
    x = i / self.pixel_len
    y = j / self.pixel_len

    return [int(x),int(y)]
