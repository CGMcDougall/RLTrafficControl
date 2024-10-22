##DONT USE##



import numpy as np
import pygame as pg

class storage:

    #init storage matrices to track locations of cars with 0,1 values 
    def __init__(self,width,height, Size = 50, Lanes = 2):
        self.lanes = Lanes

        self.width = width
        self.height = height

        self.offsetX = 20
        self.offsetY = 20

        #sets the scaling size of matrix -> (size of screen / size = # of rows/cols)
        self.size = Size
        
        #empty for now
        # self.xLocationMatrix = np.zeros((int(width/self.size),self.lanes))
        # self.yLocationMatrix = np.zeros((self.lanes,int(height/self.size)))
        self.xLen =(int(width/self.size))
        self.yLen =int(height/self.size)
        self.matrix = np.zeros((self.xLen,self.yLen))



    
    #render
    def draw(self,s : pg.Surface, mode : int = 0):

        tempWidth = self.width/2
        tempHeight = self.height/2 -self.size

        for i in range(0,self.xLen):
            for j in range(0,self.yLen):

                size = self.size/4

                loc = self.indexToCord(i,j)
                r = pg.Rect(loc[0],loc[1], size, size)

                halfX = self.xLen/2
                halfY = self.yLen/2


                #IF IN/ON ROADS !!!!
                if(i >= halfX - self.lanes/2 and i < (halfX + self.lanes/2) or j >= halfY - self.lanes/2 and j < (halfY + self.lanes/2)):
                    if mode == 1 or mode == 0:
                        pg.draw.rect(s, (200, 50, 50, .75), r)
                elif mode == 0:
                    pg.draw.rect(s, (30, 30, 30, .50), r)


        # for i in range(0,len(self.xLocationMatrix)):
        #     for j in range(0,self.lanes):
        #         r = pg.Rect((i * self.size) + 20, (j * self.size) + (self.height/2- self.size)+ 20, self.size/4,self.size/4)
        #         pg.draw.rect(s,(0,100,200,.75),r)
        #
        # for i in range(0,self.lanes):
        #     for j in range(0,len(self.yLocationMatrix[i])):
        #         r = pg.Rect((i * self.size) + (self.height/2- self.size)+ 20, (j * self.size)+20, self.size/4,self.size/4)
        #         pg.draw.rect(s,(0,200,100,.75),r)


    #TBH this sucks and im coping (DONT USE THIS)
    def locConversion(self,i,j, nw : bool = True)-> (float,float):

        if nw:
            return((i * self.size) + 20, (j * self.size) + (self.height / 2 - self.size) + 20)
        else:
            return((i * self.size) + (self.height / 2 - self.size) + 20, (j * self.size) + 20)

    #Use this instead
    def indexToCord(self,i,j):
        x = i * (self.width / self.xLen) + self.offsetX
        y = j * (self.height / self.yLen) + self.offsetY
        return (x,y)

    def getAt(self,x,y):
        x = x - self.offsetX
        x = x * (self.xLen/self.width)

        y = y - self.offsetY
        y = y * (self.yLen/self.height)

        return x,y



