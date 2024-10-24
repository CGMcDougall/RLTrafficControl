import random

import pygame as pg
import time, Car

import numpy as np
from Traffic_env.envs import Matricies as mat
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

        for event in pg.event.get():
            # check if the event is the X button
            if event.type==pg.QUIT:
                # if it is quit the game
                pg.quit()
                exit(0)

if __name__ == "__main__":
    main()
    # e = env.GridWorldEnv("human")
    # while True:
    #     e.render()

