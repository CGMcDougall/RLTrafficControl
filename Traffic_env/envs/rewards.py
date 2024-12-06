import numpy as np
from Traffic_env.envs import Matricies as mat
import random

from Traffic_env.envs.Visual import LightAction


# ~ ~ REWARD FRAMEWORK ~ ~
# What do we want to reward: 
# - crossing through the intersection
# What do we want to inhibit
# - longer time spent at intersection (discount factor(???)

# TODO:
# arrays for each lane. cars get added to the array the moment driving = false. 
# periodically count # of cars in array
# initialize timer in car class that triggers on stop event. 

# CALCULATING REWARD
# at each step: set the car's timer object to be stop_time - elapsed_time 

class Rewards:


    threshold = 45
    pos_scale = 0.5
    neg_scale = 0.5
    buffer_scale = 1.5
    def __init__(self,run_speed):
        self.fps = run_speed


    def GetReward(self,cur_action:LightAction,buffer:list,ns:list,ew:list):
            tot = 0
            #print("-----------NS:")
            ns_cars, ns_wait = self.calculate_reward(ns)
            #print("-----------EW:")
            ew_cars, ew_wait = self.calculate_reward(ew)

            #make wait times be minimum 1
            #ns_wait += 1
            #ew_wait += 1

            if cur_action == LightAction.V_GREEN:
                tot = (self.pos_scale * (ns_cars * ns_wait) - self.neg_scale*(ew_cars * ew_wait))
                tot += self.buffer_scale * self.buffer_reward(buffer)
            elif cur_action == LightAction.H_GREEN:
                tot = (self.pos_scale *(ew_cars * ew_wait) - self.neg_scale*(ns_cars * ns_wait))
                tot += self.buffer_scale * self.buffer_reward(buffer)

            else:
                tot = 0.0001 * self.neg_scale * (-(ew_cars * ew_wait))

            return tot, (ns_wait + ew_wait)/2


    def buffer_reward(self,buffer:list):
        tot = 0
        for b in buffer:
            tot += b.stoptime
        return tot

    def calculate_reward(self,array):
        stop_avg = (0.0)
        car_nums = 0

        #loop over each array and average the stoptime and also count # of cars in array 
        for car in array: 
            car_nums += 1
            stop_avg += car.stoptime 

        if car_nums != 0:
            stop_avg = stop_avg/car_nums
        #print("stop then num")
        #rint(stop_avg)
        #print(car_nums)

        return car_nums, stop_avg
