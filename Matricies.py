import numpy as np
import pygame as pg

class storage:

    #init storage matrices to track locations of cars with 0,1 values 
    def __init__(self,width,height, Size = 50, Lanes = 2):
        self.lanes = Lanes

        self.width = width
        self.height = height

        #sets the scaling size of matrix -> (size of screen / size = # of rows/cols)
        self.size = Size
        
        #empty for now
        self.xLocationMatrix = np.zeros((int(width/self.size),self.lanes))
        self.yLocationMatrix = np.zeros((self.lanes,int(height/self.size)))

    
    #render
    def draw(self,s : pg.Surface):

        tempWidth = self.width/2
        tempHeight = self.height/2 -self.size

        for i in range(0,len(self.xLocationMatrix)):
            for j in range(0,self.lanes):
                r = pg.Rect((i * self.size) + 20, (j * self.size) + (self.height/2- self.size)+ 20, self.size/4,self.size/4)
                pg.draw.rect(s,(0,100,200,.75),r)

        for i in range(0,self.lanes):
            for j in range(0,len(self.yLocationMatrix[i])):
                r = pg.Rect((i * self.size) + (self.height/2- self.size)+ 20, (j * self.size)+20, self.size/4,self.size/4)
                pg.draw.rect(s,(0,200,100,.75),r)


    #TBH this sucks and im coping
    def locConversion(self,i,j, nw : bool = True)-> (float,float):
        if nw:
            return((i * self.size) + 20, (j * self.size) + (self.height / 2 - self.size) + 20)
        else:
            return((i * self.size) + (self.height / 2 - self.size) + 20, (j * self.size) + 20)