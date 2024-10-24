import random
from enum import Enum, IntEnum
import pygame as pg
import Matricies as mat
from Traffic_env.envs import Matricies as mat
import gymnasium as gym
from gymnasium import spaces

import numpy as np

from Traffic_env.envs import Visual


##Possible Actions for agent to take
class LightAction(IntEnum):
    NWgreen = 0
    NWyellow =1
    SEgreen = 2
    SEyellow =3
    FullRed = 4


##Possible "tiles" (locations) that the env can have
class Tile(Enum):
    Empty = 0
    Car = 1
    Intersection = 2
    nan = 3

    #Print the first 2 charaters of the name
    def __str__(self):
        return self.name[:3]




#Class that functions as the enviroment
class IntersectionControl:

    def __init__(self,size = 50):
        self.lanes = 2
        self.size = size
        # self.gridRows = 50
        # self.gridCols = 50

        self.mat = mat.storage(700,700,size,self.lanes)
        self.reset()

        #IDK defualt i geuss
        self.curAction = LightAction.NWgreen



    def reset(self,seed=None):
        self.lightPos = [self.size/2,self.size/2]



    ##IF switch == true, swap to next stage of light, and return curAction
    def action(self,switch:bool) -> LightAction:

        cur = self.curAction


        if switch:
            if cur == LightAction.NWgreen:
                self.curAction = LightAction.NWyellow
            elif cur == LightAction.NWyellow:
                self.curAction = LightAction.FullRed

            elif cur == LightAction.FullRed:
                self.curAction = LightAction.SEgreen


            elif cur == LightAction.SEgreen:
                self.curAction = LightAction.SEyellow
            else:
                self.curAction = LightAction.NWgreen
        return self.curAction


    #Just call storage.draw for now
    def render(self, screen: pg.Surface):
        self.mat.draw(screen)


##DEMO main function for small testing, use main usually
if __name__=="__main__":
    background_colour = (10, 10, 220)
    (width, height) = (700, 700)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Demo')

    v = Visual.visuals(screen,width,height,50,2)

    l = IntersectionControl()
    l.render(screen)

    while True:
        screen.fill(background_colour)

        #idk random switch for now
        r = random.randint(0,200)

        rand_action = (r ==0)
        #print(rand_action)


        l.action(rand_action)
        l.render(screen)

        v.lights(int(l.curAction))
        v.draw()

        pg.display.flip()