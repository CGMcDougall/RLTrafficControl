import numpy as np
import Matricies as mat
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
    scale = 1
    def __init__(self,run_speed):
        self.fps = run_speed


    def GetReward(self,cur_action:LightAction,buffer:list,ns:list,ew:list):
            tot = 0
            print("-----------NS:")
            ns_cars, ns_wait = self.calculate_reward(ns)
            print("-----------EW:")
            ew_cars, ew_wait = self.calculate_reward(ew)

            if cur_action == LightAction.V_GREEN:
                tot = self.scale * ((ns_cars * ns_wait) - (ew_cars * ew_wait))
                #tot += self.buffer_reward(buffer)
            elif cur_action == LightAction.H_GREEN:
                tot = self.scale * ((ew_cars * ew_wait) - (ns_cars * ns_wait))
                #tot += self.buffer_reward(buffer)

            return tot


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
        print(stop_avg)
        print(car_nums)

        return car_nums, stop_avg
