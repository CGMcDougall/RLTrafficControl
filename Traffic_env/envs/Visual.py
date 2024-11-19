import pygame as pg
from enum import Enum

# Load the correct pngs

class LightAction(Enum):
    V_GREEN = 0
    V_YELLOW = 1
    H_GREEN = 2
    H_YELLOW = 3
    ALL_RED = 4

class visuals:

    Inter = pg.image.load("Assets/Intersection.png")
    Is = (100,100)
    Inter = pg.transform.scale(Inter,Is)

    road = pg.image.load("Assets/Road.png")
    Rs = (50,30)
    road = pg.transform.scale(road,Rs)
    downRoad = pg.transform.rotate(road,90)

    VGreen = pg.image.load("Assets/VGreen.png")
    VGreen = pg.transform.scale(VGreen, Is)
    HGreen = pg.image.load("Assets/HGreen.png")
    HGreen = pg.transform.scale(HGreen, Is)

    HYellow = pg.image.load("Assets/HYellow.png")
    HYellow = pg.transform.scale(HYellow, Is)
    VYellow = pg.image.load("Assets/VYellow.png")
    VYellow = pg.transform.scale(VYellow, Is)

    AllRed = pg.image.load("Assets/AllRed.png")
    AllRed = pg.transform.scale(AllRed,Is)

    curLight = None

    def __init__(self,s : pg.surface , screen_size = 700, mat_size = 14, Lanes = 2):
        self.screen_size = screen_size
        self.screen = s
        self.mat_size = mat_size
        self.lanes = Lanes
        self.tile_size = screen_size/mat_size

    # Numbers need to be updated so that they're not hard coded in 
    # But otherwise this works fine as the main render
    def draw(self):
        for i in range (0,self.mat_size):
            for j in range (0,self.lanes):
                self.screen.blit(self.road,(i * self.tile_size, self.screen_size/2 - 35 + (40 * j)))

        for i in range (0, self.mat_size):
            for j in range(0,self.lanes):
                self.screen.blit(self.downRoad,(self.screen_size/2 - 35 + (40 * j), i * self.tile_size ))

        self.screen.blit(self.Inter, (self.screen_size/2-self.tile_size, self.screen_size/2-self.tile_size))
        if(self.curLight != None):
            self.screen.blit(self.curLight,(self.screen_size/2-self.tile_size, self.screen_size/2-self.tile_size))

    # Takes a LightAction, phase and sets the appropirate spirte to be drawn
    def lights(self, phase):
        if phase == LightAction.V_GREEN:
            self.curLight = self.VGreen
        elif phase == LightAction.V_YELLOW:
            self.curLight = self.VYellow
        elif phase == LightAction.H_GREEN:
            self.curLight = self.HGreen
        elif phase == LightAction.H_YELLOW:
            self.curLight = self.HYellow
        else:
            self.curLight = self.AllRed

