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

    def __init__(self,s : pg.surface ,width,height,Size =50, Lanes = 2):
        self.width = width
        self.height = height
        self.screen = s
        self.size = Size
        self.lanes = Lanes

    # Numbers need to be updated so that they're not hard coded in 
    # But otherwise this works fine as the main render
    def draw(self):
        for i in range (0,int(self.width/self.size)):
            for j in range (0,self.lanes):
                self.screen.blit(self.road,(i * 50, self.height/2 - 35 + (40 * j)))

        for i in range (0, int(self.height/self.size)):
            for j in range(0,self.lanes):
                self.screen.blit(self.downRoad,(self.height/2 - 35 + (40 * j), i * 50 ))

        self.screen.blit(self.Inter, (self.width/2-50, self.height/2-50))
        if(self.curLight != None):
            self.screen.blit(self.curLight,(self.width/2-50, self.height/2-50))

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

