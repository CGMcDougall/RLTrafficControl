import pygame as pg
from enum import Enum

from Traffic_env.envs import Matricies
import numpy as np

from Traffic_env.envs.Visual import LightAction


class CarDirs(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

#car class
class car:
    speed = 0.05
    color = (250,250,250,1)
    driving = True

    # Initialize a screen position, matrix location, and direction
    def __init__(self, start_dir):
        self.Car = pg.Rect(320,0,20,20)
        self.dir = [0.0,1.0]
        if start_dir == CarDirs.UP:
            self.Car = pg.Rect(320,0,20,20)
            self.dir = [0.0,1.0]
            self.loc = [700/50/2-1,0]
        elif start_dir == CarDirs.LEFT:
            self.Car = pg.Rect(0,360,20,20)
            self.dir = [1.0,0.0]
            self.loc = [0,700/50/2]
        elif start_dir == CarDirs.RIGHT:
            self.Car = pg.Rect(700,320,20,20)
            self.dir = [-1.0,0.0]
            self.loc = [700/50-1,700/50/2-1]
        elif start_dir == CarDirs.DOWN:
            self.Car = pg.Rect(360,700,20,20)
            self.dir = [0.0,-1.0]
            self.loc = [700/50/2,700/50-1]
    
    def draw(self,s : pg.surface):
        pg.draw.rect(s,self.color,self.Car)

    def act(self, mat : Matricies):


        if self.driving == False:
            return

        # Speed and dt are no longer used, which I think is fine because I'm calling tick with an fps in main?
        # But can look more into that later, also low prio
        self.Car = self.Car.move(self.dir)
        if self.dir[0] == 0:
            self.loc[1] = Matricies.getAt(mat, self.Car.x, self.Car.y)[1]
        else:
            self.loc[0] = Matricies.getAt(mat, self.Car.x, self.Car.y)[0]

    # A function to get clamped (int) value for location in matrix
    def getMatPos(self):
        return int(self.loc[1]), int(self.loc[0])



    def legalMoveCheck(self,mat : Matricies,phase) ->bool:
        self.atLight(mat,phase)
        #self.avaliableSpot(mat)
        return self.driving

    def avaliableSpot(self, mat :Matricies):

        if(mat.getBordering(self.loc,self.dir) == 1):
            self.driving = False

        # n = mat.getNeighbors(self.loc)
        # #print(n)
        # for a in n:
        #     movingTo = [self.loc[0] + self.dir[0], self.loc[1] + self.dir[1]]
        #     #print(a)
        #     #print(movingTo)
        #     if a.all(movingTo):
        #         #Stop
        #         driving = False
        #         return


    #Stops the car if at an intersections and light phase is red/yellow
    def atLight(self, mat : Matricies, phase):
        IBX = mat.IBX
        IBY = mat.IBY

        if abs(self.dir[0]) == 1 and phase == LightAction.H_GREEN:
            self.driving = True
            return
        if abs(self.dir[1]) == 1 and phase == LightAction.V_GREEN:
            self.driving = True
            return




        if self.dir == [1.0,0.0]:
            if(self.loc[0] == (IBX[0]-1)):
                self.driving = False
        elif self.dir == [-1.0,0.0]:
            if(self.loc[0] == (IBX[1]-1)):
                self.driving = False
                return
        elif self.dir == [0.0,1.0]:

            if(self.loc[1] == (IBY[0]-1)):
                self.driving = False
                return
        elif self.dir == [0.0,-1.0]:

            if(self.loc[1] == (IBY[1]-1)):
                self.driving = False
                return










