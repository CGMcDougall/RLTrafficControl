import random

import pygame as pg
import time, Car
from Car import CarDirs

from data import Data as pd



import numpy as np
from Traffic_env.envs import Matricies as mat
from Traffic_env.envs import MonoIntersection as env
from Traffic_env.envs.MonoIntersection import Actions
from Traffic_env.envs import Visual

#return change in time and new real time
def time_consistency(oldtime : float):
    dt = (time.time()-oldtime)
    return dt, (oldtime + dt)

def main():
    # #Screen Setup
    # background_colour = (120, 120, 120)
    # screen_size = 700 # Should probably set this as a const somewhere
    # screen = pg.display.set_mode((screen_size, screen_size))
    # pg.display.set_caption("Lil Traffic Light Fella")
    running = True

    #info setup
    mat_size = 14
    Lanes = 2


    #Viusal Setup
    #v = Visual.visuals(screen,screen_size,mat_size,Lanes)

    #Enviroment SetUp
    monoInt = env.IntersectionControl(mat_size,Lanes,"human")

    #Data
    Data = pd()

    while running:

        monoInt.render()
        monoInt.action()

        #Delete Later
        if random.randint(0,50) == 1:
                Data.addToQueue(random.randint(0,10),pg.time.get_ticks()/1000)

        monoInt.step()


        print(mat.storage.ns_array)
        # Update light display
        #v.lights(monoInt.action_loop[monoInt.curLight])



        #
        # for event in pg.event.get():
        # # check if the event is the X button
        #     if event.type==pg.QUIT:
        #     # if it is quit the game
        #         pg.quit()
        #         exit(0)
        #     elif event.type == pg.KEYDOWN:
        #         # Check if the Escape key is pressed
        #         if event.key == pg.K_ESCAPE:
        #             running = False  # Exit the loop
        #             pg.quit()
        #             Data.plot()

if __name__ == "__main__":
    main() # The code beneath with the world env stuff does eventually need to work I think
    # Just for project requirements and whatnot, but low prio


    # e = env.GridWorldEnv("human")
    # while True:
    #     e.render()

