import random

import pygame as pg
import time, Car
from Car import CarDirs

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
    #Screen Setup
    background_colour = (120, 120, 120)
    (width, height) = (700, 700) # Should probably set this as a const somewhere
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

    #Viusal Setup
    v = Visual.visuals(screen,width,height,Size,Lanes)

    #Enviroment SetUp
    monoInt = env.IntersectionControl(v,Size)

    while running:
        clock.tick(fps) # This is how it's supposed to be done but may or may not be useful to us
        dt, time_cons = time_consistency(oldtime) # Not a real dt, being used to track time between light switches, should probably be renamed for clarity
        screen.fill(background_colour)

        # Switch lights every 10 seconds for now
        if dt >= 1:
            monoInt.curAction = Actions.SWITCH
            oldtime = time_cons
        else:
            monoInt.curAction = Actions.STAY
        monoInt.action()
        monoInt.render()

        # Every frame there's a chance to spawn a car coming from a random direction
        rand_num = random.randint(0,800)
        if rand_num == 1:
            monoInt.cars.append(Car.car(CarDirs.UP))
        elif rand_num == 2:
            monoInt.cars.append(Car.car(CarDirs.DOWN))
        elif rand_num == 3:
            monoInt.cars.append(Car.car(CarDirs.LEFT))
        elif rand_num == 4:
            monoInt.cars.append(Car.car(CarDirs.RIGHT))
        
        # Loop through every car in existence and move it
        # Eventually there should be a way to check if a car has moved off screen and delete it
        for car in monoInt.cars:
            car.act(monoInt.mat)
            car.draw(screen)

        # Update light display
        v.lights(monoInt.action_loop[monoInt.curLight])

        pg.display.flip()

        for event in pg.event.get():
            # check if the event is the X button
            if event.type==pg.QUIT:
                # if it is quit the game
                pg.quit()
                exit(0)

if __name__ == "__main__":
    main() # The code beneath with the world env stuff does eventually need to work I think
    # Just for project requirements and whatnot, but low prio

    # e = env.GridWorldEnv("human")
    # while True:
    #     e.render()

