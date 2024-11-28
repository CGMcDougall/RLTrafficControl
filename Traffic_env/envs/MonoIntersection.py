import random
from enum import Enum
import pygame as pg
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
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, v: Visual.visuals,screen_size = 700, mat_size = 14,render_mode=None):

        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, mat_size, shape=(2,), dtype=int)
            }
        )

        self.curAction = 0
        self.lanes = 2
        self.size = mat_size
        self.visual = v

        # Since the lights must change in a specific order, I figured I'd just hardcode them in
        self.action_loop = [LightAction.V_GREEN, 
                            LightAction.V_YELLOW, 
                            LightAction.ALL_RED, 
                            LightAction.H_GREEN, 
                            LightAction.H_YELLOW, 
                            LightAction.ALL_RED]

        self.mat = mat.storage(screen_size,mat_size,self.lanes)
        self.reset()

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def _get_obs(self):
        return

    def step(self,act = 0):

        self.curAction = act
        self.action()

        terminated = False
        reward = 0 #self.reward()?
        obs = self._get_obs()

        return obs, reward, terminated, False

    def reset(self):
        self.curAction = Actions.STAY
        self.curLight = 0
        self.cars = []

    # IF the agent is taking the SWITCH action, swap to next stage of light
    def action(self):
        if self.curAction == Actions.SWITCH:
            if self.curLight == len(self.action_loop) - 1:
                self.curLight = 0
            else:
                self.curLight += 1

    def render(self):
        self.visual.draw()



##DEMO main function for small testing, use main usually
if __name__=="__main__":
    background_colour = (10, 10, 10)
    (width, height) = (700, 700)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Demo')

    v = Visual.visuals(screen,width,height,50,2)

    l = IntersectionControl()
    l.render(screen)

    while True:
        screen.fill(background_colour)

        #idk random switch for now
        r = random.randint(0,200)

        rand_action = (r ==0)
        #print(rand_action)


        l.action(rand_action)
        l.render(screen)

        v.lights(int(l.curAction))
        v.draw()

        pg.display.flip()