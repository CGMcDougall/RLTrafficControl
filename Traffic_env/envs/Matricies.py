import numpy as np
import pygame as pg
from enum import Enum
from data import Data as pd

##Possible "tiles" (locations) that the env can have
class Tile(Enum):
    ROAD = 0
    CAR = 1
    INTER = 2  # Intersection
    OCC_INTER = 3  # Occupied Intersection
    NAN = 4


class storage:

    # init storage matrices to track locations of cars with 0,1 values
    ns_array = []
    ew_array = []
    reward_buffer = []      #Matrix to store the cars that have passed through this frame

    #init storage matrices to track locations of cars with 0,1 values 
    def __init__(self, screen_size = 700, mat_size = 14, Lanes = 2):

        self.lanes = Lanes
        self.screen_size = screen_size
        self.mat_size = mat_size

        self.Data = pd()

        # Pixel lengths
        self.pixel_len = (int(screen_size / self.mat_size))

        # Initialize as empty tiles, and then fill out the roads with the correct number of lanes
        self.matrix = np.full((self.mat_size, self.mat_size), 0)
        self.inter_bound = (int(self.mat_size / 2) - 1, int(self.mat_size / 2))

        for i in range(self.inter_bound[0], self.inter_bound[1] + 1):
            for j in range(self.inter_bound[0], self.inter_bound[1] + 1):
                self.matrix[i, j] = 2



    def getBordering(self,loc,dir):
        x = int(loc[0] + dir[0])
        y = int(loc[1] + dir[1])

        if (x < 0 or x >= self.mat_size) or (y < 0 or y >= self.mat_size):
            return 0

        return self.matrix[y, x]


    def withinIntersectionBounds(self,loc) -> bool:

        x = int(loc[0])
        y = int(loc[1])
        # print(self.inter_bound[0],self.inter_bound[1])

        return (self.inter_bound[0] <= x and self.inter_bound[1] >= x and self.inter_bound[0] <= y and self.inter_bound[1] >= y)

    def GetCarsWithinRange(self,r : int = 2):
        all = []
        for i in range(1,r+1):
            all.append(self.matrix[self.inter_bound[0]-i,self.inter_bound[0]])
            all.append(self.matrix[self.inter_bound[1]+i, self.inter_bound[1]])

            all.append(self.matrix[self.inter_bound[1], self.inter_bound[0]-i])
            all.append(self.matrix[self.inter_bound[0] + i, self.inter_bound[1]+i])

        return all

# Helper Functions
def indexToCord(self, i, j):
    x = i * self.pixel_len
    y = j * self.pixel_len
    return (x, y)


def cordToIndex(self, i, j):
    x = i / self.pixel_len
    y = j / self.pixel_len

    return [int(x), int(y)]

