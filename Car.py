import pygame as pg
from enum import Enum

from Traffic_env.envs import Matricies
import numpy as np
import time

from Traffic_env.envs.Visual import LightAction


class CarDirs(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


# car class
class car:
    speed = 0.05
    color = (250, 250, 250, 1)
    driving = True
    size = 20
    stoptime = 0.0
    keep_drive = False

    # Initialize a screen position, matrix location, and direction
    def __init__(self, start_dir):
        self.Car = pg.Rect(320, 0, self.size, self.size)
        self.dir = [0.0, 1.0]
        if start_dir == CarDirs.UP:
            self.Car = pg.Rect(320, 0, self.size, self.size)
            self.dir = [0.0, 1.0]
            self.loc = [14 / 2 - 1, 0]
        elif start_dir == CarDirs.LEFT:
            self.Car = pg.Rect(0, 360, self.size, self.size)
            self.dir = [1.0, 0.0]
            self.loc = [0, 14 / 2]
        elif start_dir == CarDirs.RIGHT:
            self.Car = pg.Rect(700, 320, self.size, self.size)
            self.dir = [-1.0, 0.0]
            self.loc = [14 - 1, 14 / 2 - 1]
        elif start_dir == CarDirs.DOWN:
            self.Car = pg.Rect(360, 700, self.size, self.size)
            self.dir = [0.0, -1.0]
            self.loc = [14 / 2, 14 - 1]

    def draw(self, s: pg.surface):
        pg.draw.rect(s, self.color, self.Car)

<<<<<<< Updated upstream
    def act(self, mat: Matricies, t: float = 0):
=======
    def act(self, mat : Matricies,tot_time:float, t : float = 0):
        ns_array = mat.ns_array
        ew_array = mat.ew_array
>>>>>>> Stashed changes

        ##IF NOT DRIVING
        if self.driving == False:
            self.stoptime += t
<<<<<<< Updated upstream
            return
=======
            if (abs(self.dir[0]) == 1 and self not in ew_array):
                ew_array.append(self)
            if (abs(self.dir[1]) == 1 and self not in ns_array):
                ns_array.append(self)
            return 
        
        #car is moving, so if it is in one of the arrays, check if its within intersection bounds 
        #if so, remove from array 
        if mat.withinIntersectionBounds(self.loc):
            self.keep_drive = True

            #mat.Data.addToQueue(self.stoptime,tot_time)
            mat.reward_buffer.append(self)

            if(self in ew_array):
                ew_array.remove(self)
            if(self in ns_array):
                ns_array.remove(self)
>>>>>>> Stashed changes

        # Speed and dt are no longer used, which I think is fine because I'm calling tick with an fps in main?
        # But can look more into that later, also low prio
        self.Car = self.Car.move(self.dir)
        if self.dir[0] == 0:
            self.loc[1] = Matricies.cordToIndex(mat, self.Car.x, self.Car.y)[1]
        else:
            self.loc[0] = Matricies.cordToIndex(mat, self.Car.x, self.Car.y)[0]

    # A function to get clamped (int) value for location in matrix
    def getMatPos(self):
        return int(self.loc[1]), int(self.loc[0])

    def legalMoveCheck(self, mat: Matricies, phase):

        l = self.notAtLight(mat, phase)
        i = self.avaliableSpot(mat)
        self.driving = (l and i) or (self.MoveRegardless(mat, phase))

    # If boardering spot doesnt have a car in it (ie x != 1,4), return true
    def avaliableSpot(self, mat: Matricies) -> bool:
        if mat.getBordering(self.loc, self.dir) == 1 or mat.getBordering(self.loc, self.dir) == 3:
            return False
        return True

    # If the light is green, or past the light, drive anyway, regardless of light phase
    def MoveRegardless(self, mat, phase) -> bool:

        if abs(self.dir[0]) == 1 and phase == LightAction.H_GREEN:
            return True
        if abs(self.dir[1]) == 1 and phase == LightAction.V_GREEN:
            return True

        # If gets this far, keep driving if in intersection, otherwise stop
        return self.keep_drive

    # Stops the car if at an intersections and light phase is not green
    def notAtLight(self, mat, phase):
        # if bordering road, ie (x < 2, 3), not at intersection
        return (mat.getBordering(self.loc, self.dir) < 2)








