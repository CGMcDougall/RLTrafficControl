import random
import time
from enum import Enum
from typing import Optional

import pygame as pg

import Car
from Traffic_env.envs import Matricies as mat
import gymnasium as gym
from gymnasium import spaces

import numpy as np

from Traffic_env.envs import Visual
from Traffic_env.envs.Visual import LightAction


# Possible Actions the agent can take
class Actions(Enum):
    STAY = 0
    SWITCH = 1

#Class that functions as the enviroment
class IntersectionControl(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array","None"], "render_fps": 4}

    run_speed = 6000 #By increasing FPS, we can increase the speed of the simulation, but some other variables need to updated to work with fps


    # Time Setup
    clock = pg.time.Clock()
    oldtime = time.time()
    screen_size = 700

    def __init__(self, mat_size = 14,Lanes = 2, render_mode=None):

        ## If we observe the first space before the intersection of every oncoming lane, we would have 2^4 = 16 states
        ## if we look at the first two of every lane would be 2^8 = 256 states
        self.n_states = 256
        self.n_actions = 2
        self.to_cell, self.to_state = self.makeStateMapping() ##To_Cell maps binary to State #, To_state maps # to []
        print(len(self.to_cell))

        #print(self.to_state["00100000"])
        #print(self.to_cell[self.to_state["00100000"]])

        # self.observation_space = spaces.Dict(
        #     {
        #         "agent": spaces.Box(0, mat_size, shape=(2,), dtype=int)
        #     }
        # )

        self.curAction = 0
        self.lanes = 2
        self.size = mat_size

        # Since the lights must change in a specific order, I figured I'd just hardcode them in
        self.action_loop = [LightAction.V_GREEN,
                            LightAction.V_YELLOW,
                            LightAction.ALL_RED,
                            LightAction.H_GREEN,
                            LightAction.H_YELLOW,
                            LightAction.ALL_RED]

        self.mat = mat.storage(self.screen_size,mat_size,self.lanes)
        self.reset()

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        if render_mode != "None" and render_mode != None:
            self.screen = pg.display.set_mode((self.screen_size, self.screen_size))
            self.visual = Visual.visuals(self.screen, self.screen_size, mat_size, Lanes)
            pg.display.set_caption("Lil Traffic Light Fella")


    def _get_obs(self):
        return

    def step(self,act = 0):

        self.curAction = act


        terminated = False
        reward = 0.5 #self.reward()?
        obs = self._get_obs()

        return obs, reward, terminated, False

    def reset(self,seed: Optional[int] = None, options: Optional[dict] = None):

        super().reset(seed=seed)

        self.curAction = Actions.STAY
        self.curLight = 0
        self.cars = []

        return [0,0,0,0,0,0,0,0], self.curLight


    # IF the agent is taking the SWITCH action, swap to next stage of light
    def action(self):
        self.clock.tick(self.run_speed)  # This is how it's supposed to be done but may or may not be useful to us
        self.Env_Act()

        if self.curAction == Actions.SWITCH:
            if self.curLight == len(self.action_loop) - 1:
                self.curLight = 0
            else:
                self.curLight += 1

    def render(self):
        if self.render_mode == "None" or self.render_mode == None:
            return
        self.screen.fill((120, 120, 120))
        self.visual.draw()
        self.CarsDrivingVisual(self.screen)
        pg.display.flip()

    ##HELPER FUNCTIONS
    def GetMappingIndex(self, s):
        val = ""
        for i in s:
            val += str(i)
        return self.to_state[val]

    def makeStateMapping(self):
        ##Maybe have the states map to a dictionary of size 256
        ##Use binary to int maybe?? >> Binary: 11111111 -->  Int: 255
        StateList = []
        mapping = {}

        ##Dictinary mapping
        for i in range(self.n_states):
            val = str(bin(i)[2:])
            val = val.zfill(8)
            temp = []
            for c in val:
                temp.append(int(c))

            StateList.append(temp)
            mapping[(val)] = i

        flipped_mapping = {v: k for k, v in mapping.items()}  # maps state # to binary number (i hope)
        return flipped_mapping, mapping


    ##Env generation/update things things
    def time_consistency(self,ot: float):
        dt = (time.time() - ot)
        return dt, (ot + dt)

    def Env_Act(self):

        ##TEMPORARY
        rand_num = random.randint(0, 400)
        if rand_num == 1 and self.mat.matrix[int(700 / 50 / 2) - 1, 0] == 0:
            self.cars.append(Car.car(Car.CarDirs.UP))
        elif rand_num == 2 and self.mat.matrix[int(700 / 50 / 2), int(700 / 50) - 1] == 0:
            self.cars.append(Car.car(Car.CarDirs.DOWN))
        elif rand_num == 3 and self.mat.matrix[0, int(700 / 50 / 2)] == 0:
            self.cars.append(Car.car(Car.CarDirs.LEFT))
        elif rand_num == 4 and self.mat.matrix[int(700 / 50) - 1, int(700 / 50 / 2) - 1] == 0:
            self.cars.append(Car.car(Car.CarDirs.RIGHT))

        rand_num2 = random.randint(0, 400)
        if rand_num2 == 1:
            self.curAction = Actions.SWITCH
        else:
            self.curAction = Actions.STAY

    def CarsDrivingVisual(self, screen):

        dt, time_cons = self.time_consistency(
            self.oldtime)  # Not a real dt, being used to track time between light switches, should probably be renamed for clarity
        self.oldtime = time_cons

        # Loop through every car in existence and move it
        for car in self.cars:
            # If Car is within the intersection, set to empty intersection instead of empty road
            if self.mat.withinIntersectionBounds(car.getMatPos()):
                self.mat.matrix[car.getMatPos()] = 2
            else:
                self.mat.matrix[car.getMatPos()] = 0

            car.legalMoveCheck(self.mat, self.action_loop[self.curLight])
            car.act(self.mat, dt)

            if car.loc[0] >= self.mat.mat_size or car.loc[1] >= self.mat.mat_size or car.loc[0] < 0 or car.loc[1] < 0:
                print(car.stoptime)
                self.cars.remove(car)
            else:
                if self.mat.withinIntersectionBounds(car.getMatPos()):
                    self.mat.matrix[car.getMatPos()] = 3
                else:
                    self.mat.matrix[car.getMatPos()] = 1
            car.draw(screen)
        self.visual.lights(self.action_loop[self.curLight])


##DEMO main function for small testing, use main usually
if __name__=="__main__":

    running = True

    # info setup
    mat_size = 14
    Lanes = 2

    monoInt = IntersectionControl(mat_size, Lanes, "human")

    while running:
        monoInt.render()
        monoInt.action()
        monoInt.step()
