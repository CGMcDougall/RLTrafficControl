import pygame as pg
from enum import Enum

from Traffic_env.envs import Matricies
import numpy as np

class CarDirs(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

#car class
class car:
    speed = 0.05
    color = (250,250,250,1)

    # Initialize a location and direction
    # loc variable has been temporarily removed
    # I'd suggest bringing it back eventually but using it to track matrix location directly
    def __init__(self, start_dir):
        self.Car = pg.Rect(320,0,20,20)
        self.dir = [0.0,1.0]
        if start_dir == CarDirs.UP:
            self.Car = pg.Rect(320,0,20,20)
            self.dir = [0.0,1.0]
        elif start_dir == CarDirs.LEFT:
            self.Car = pg.Rect(0,360,20,20)
            self.dir = [1.0,0.0]
        elif start_dir == CarDirs.RIGHT:
            self.Car = pg.Rect(700,320,20,20)
            self.dir = [-1.0,0.0]
        elif start_dir == CarDirs.DOWN:
            self.Car = pg.Rect(360,700,20,20)
            self.dir = [0.0,-1.0]

    def draw(self,s : pg.surface):
        pg.draw.rect(s,self.color,self.Car)

    def act(self, mat : Matricies):
        # Pygame already has a move rectangle function, might as well use it
        # Speed and dt are no longer used, which I think is fine because I'm calling tick with an fps in main?
        # But can look more into that later, also low prio
        self.Car = self.Car.move(self.dir)

    #maybe a function to get clamped (int) value for location in matrix
    # Probably not necessary anymore later if we just have self.loc mean matric location
    def getMatPos(self):
        return int(self.loc[0]), int(self.loc[1])



