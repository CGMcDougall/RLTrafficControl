import random

import pygame as pg
import time, Car, Intersection

import numpy as np
import Matricies as mat
#from Traffic_env.envs import grid_world as env
from Traffic_env.envs import MonoIntersection as env
from Traffic_env.envs import Visual


#return change in time and new real time
def time_consistency(oldtime : float):
    dt = (time.time()-oldtime)
    return dt, (oldtime + dt) 




def main():
    #Screen Setup
    background_colour = (10, 10, 220)
    (width, height) = (700, 700)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Demo')
    running = True

    #info setup
    Size = 50
    Lanes = 2

    #Time Setup
    clock = pg.time.Clock()
    oldtime = time.time()
    fps = 60

    #Enviroment SetUp
    monoInt = env.IntersectionControl(Size)

    #Viusal Setup
    v = Visual.visuals(screen,width,height,Size,Lanes)

    while running:
        screen.fill(background_colour)

        # idk random switch for now
        r = random.randint(0, 200)
        rand_action = (r == 0)


        monoInt.action(rand_action)
        monoInt.render(screen)

        v.lights(int(monoInt.curAction))
        v.draw()

        pg.display.flip()



# def main():
#
#     #Important Setup
#     Size = 50;
#     Lanes =2;
#
#     #renderMode     //FOR determining how much hud should be rendered
#     mode = 1
#
#     #Screen Setup
#     background_colour = (10,10,220)
#     (width, height) = (700, 700)
#     screen = pg.display.set_mode((width, height))
#     pg.display.set_caption('Demo')
#
#     Mat = mat.storage(width,height,Size, Lanes)
#
#     #time setup
#     clock = pg.time.Clock()
#     oldtime = time.time()
#     fps = 60
#
#     #Intersection
#     I = Intersection.intersection()
#
#     #Visual Elements
#     v = Visual.visuals(screen,width,height,Size,Lanes)
#
#
#     #pg.rect(screen,(0,0,0),Car)
#     print(Mat.locConversion(0,0))
#     c = Car.car(Mat.locConversion(0,0))
#
#
#     running = True
#
#     hud = True
#
#     #Main Engine Loop
#     while running:
#
#         # time (for consistence across devices)
#         clock.tick(fps)
#         dt, oldtime = time_consistency(oldtime)
#
#
#         #Required to "clean Screen"
#         screen.fill(background_colour)
#
#         #Check Update intersection
#         nw, se = I.act(dt)
#
#         #Base layer should be visuals
#         v.lights(nw,se)
#         v.draw()
#
#
#
#         Mat.draw(screen,mode)
#
#
#         c.act(dt,Mat)
#         c.draw(screen)
#
#         #for events like key clicking
#         for event in pg.event.get():
#
#             if event.type == pg.KEYUP:
#                 if pg.K_TAB:
#                     mode += 1
#                     mode = mode % 3
#                     hud = not hud
#
#             if event.type == pg.QUIT:
#                 running = False
#
#
#         #Required to render
#         pg.display.flip()


if __name__ == "__main__":
    main()
    # e = env.GridWorldEnv("human")
    # while True:
    #     e.render()

