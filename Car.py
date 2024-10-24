import pygame as pg

from Traffic_env.envs import Matricies
import numpy as np

#car class
class car:

    loc = (0.0,0.0)

    speed = 50
    color = (0,0,0,1)

    def __init__(self, pos: (float,float)):
        self.Car = pg.Rect(pos[0],pos[1],20,20)
        self.loc = (pos[0],pos[1])



    def draw(self,s : pg.surface):
        pg.draw.rect(s,self.color,self.Car)


    #supply with dt to have uniform movement between all cars
    def act(self,dt: float, mat : Matricies):
        dir = (1.0,0.0)

        self.loc += np.array(dir) * float(self.speed) * dt

        self.Car.x = self.loc[0]
        self.Car.y = self.loc[1]


        #self.Car.x += self.speed * dt





    #maybe a function to get clamped (int) value for location in matrix
    def getMatPos(self):
        return int(self.loc[0]), int(self.loc[1])



