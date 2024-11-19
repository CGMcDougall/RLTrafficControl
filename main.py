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
    screen_size = 700 # Should probably set this as a const somewhere
    screen = pg.display.set_mode((screen_size, screen_size))
    pg.display.set_caption('Demo')
    running = True

    #info setup
    mat_size = 14
    Lanes = 2

    #Time Setup
    clock = pg.time.Clock()
    oldtime = time.time()
    fps = 60

    #Viusal Setup
    v = Visual.visuals(screen,screen_size,mat_size,Lanes)

    #Enviroment SetUp
    monoInt = env.IntersectionControl(v,screen_size,mat_size)

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

        # Every frame there's a chance to spawn a car coming from a random direction (CarDirs refers to where it is COMING FROM)
        rand_num = random.randint(0,400)
        if rand_num == 1 and monoInt.mat.matrix[int(700/50/2)-1,0] == 0:
            monoInt.cars.append(Car.car(CarDirs.UP))
        elif rand_num == 2 and monoInt.mat.matrix[int(700/50/2),int(700/50)-1] == 0:
            monoInt.cars.append(Car.car(CarDirs.DOWN))
        elif rand_num == 3 and monoInt.mat.matrix[0,int(700/50/2)] == 0:
            monoInt.cars.append(Car.car(CarDirs.LEFT))
        elif rand_num == 4 and monoInt.mat.matrix[int(700/50)-1,int(700/50/2)-1] == 0:
            monoInt.cars.append(Car.car(CarDirs.RIGHT))

        # Loop through every car in existence and move it
        for car in monoInt.cars:
            #If Car is within the intersection, set to empty intersection instead of empty road
            if monoInt.mat.withinIntersectionBounds(car.getMatPos()):
                monoInt.mat.matrix[car.getMatPos()] = 2
            else:
                monoInt.mat.matrix[car.getMatPos()] = 0

            car.legalMoveCheck(monoInt.mat, monoInt.action_loop[monoInt.curLight])
            car.act(monoInt.mat)

            if car.loc[0] >= monoInt.mat.mat_size or car.loc[1] >= monoInt.mat.mat_size or car.loc[0] < 0 or car.loc[1] < 0:
                monoInt.cars.remove(car)
            else:
                if monoInt.mat.withinIntersectionBounds(car.getMatPos()):
                    monoInt.mat.matrix[car.getMatPos()] = 3
                else:
                    monoInt.mat.matrix[car.getMatPos()] = 1
                car.draw(screen)

        #print(monoInt.mat.matrix)
        # Update light display
        v.lights(monoInt.action_loop[monoInt.curLight])

        pg.display.flip()
        for event in pg.event.get():
        # check if the event is the X button
            if event.type==pg.QUIT:
            # if it is quit the game
                pg.quit()
                exit(0)

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

