import pygame as pg


#car class
class car:




    speed = 50
    color = (0,0,0,1)

    def __init__(self, pos: (float,float)):
        self.Car = pg.Rect(pos[0],pos[1],20,20)



    def draw(self,s : pg.surface):
        pg.draw.rect(s,self.color,self.Car)


    #supply with dt to have uniform movement between all cars
    def act(self,dt: float):
        self.Car.x += self.speed * dt


    #maybe a function to get clamped (int) value for location in matrix
    def getMatPos(self):
        return int(self.Car.x), int(self.Car.y)



