import pygame as pg



#import Assets as As


class visuals:

    Inter = pg.image.load("Assets/Intersection.png")
    Is = (100,100)
    Inter = pg.transform.scale(Inter,(100,100))


    road = pg.image.load("Assets/Road.png")
    Rs = (50,30)
    road = pg.transform.scale(road,Rs)
    downRoad = pg.transform.rotate(road,90)

    lightScale = (100,100)

    GreenNW = pg.image.load("Assets/GreenNW.png")
    GreenNW = pg.transform.scale(GreenNW, lightScale)
    GreenSE = pg.image.load("Assets/GreenSE.png")
    GreenSE = pg.transform.scale(GreenSE, lightScale)

    YellowSE = pg.image.load("Assets/YellowSE.png")
    YellowSE = pg.transform.scale(YellowSE, lightScale)
    YellowNW = pg.image.load("Assets/YellowNW.png")
    YellowNW = pg.transform.scale(YellowNW, lightScale)

    RedNWSE = pg.image.load("Assets/RedNWSE.png")
    RedNWSE = pg.transform.scale(RedNWSE,lightScale)

    curLight = None

    def __init__(self,s : pg.surface ,width,height,Size =50, Lanes = 2):
        self.width = width
        self.height = height
        self.screen = s
        self.size = Size
        self.lanes = Lanes



    def draw(self):

        for i in range (0,int(self.width/self.size)):
            for j in range (0,self.lanes):
                self.screen.blit(self.road,(i * 50, self.height/2 - 35 + (40 * j)))

        for i in range (0, int(self.height/self.size)):
            for j in range(0,self.lanes):
                self.screen.blit(self.downRoad,(self.height/2 - 35 + (40 * j), i * 50 ))

        self.screen.blit(self.Inter, (self.width / 2  - 50, self.height / 2 - 50))

        if(self.curLight != None):
            self.screen.blit(self.curLight,(500,500))



    # Takes a LightAction, phase and sets the appropirate spirte to be drawn
    def lights(self, phase:int):
        pos = (300,300)


        #print(phase)

        if phase == 0:
            self.curLight = self.GreenNW
        elif phase == 1:
            self.curLight = self.YellowNW
        elif phase == 2:
            self.curLight = self.GreenSE
        elif phase == 3:
            self.curLight = self.YellowSE
        else:
            self.curLight = self.RedNWSE

