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
    pos_scale = 1
    neg_scale = 0.5
    buffer_scale = 9
    def __init__(self,run_speed):
        self.fps = run_speed


    def GetReward(self,cur_action:LightAction,act,buffer:list,ns:list,ew:list):
            return self.reward_calc_1(cur_action,act,buffer,ns,ew)

            #return self.reward_calc_2(cur_action,act, buffer, ns, ew)



    def reward_calc_2(self,cur_action:LightAction,act,buffer:list,ns:list,ew:list):
        tot = 0
        ns_cars, ns_wait = self.calculate_reward(ns)
        ew_cars, ew_wait = self.calculate_reward(ew)


        #Cost of switching
        if act == 1:
            tot -= 5

        #Longer wait time bad
        wait_time_tot = 0
        for a in (ns + ew):
            wait_time_tot += a.stoptime

        tot -= ns_cars + ew_cars
        tot -= wait_time_tot

        tot += len(buffer)

        return tot, (ns_wait + ew_wait) / 2



    def reward_calc_1(self,cur_action:LightAction,act,buffer:list,ns:list,ew:list):
        tot = (act * -5)


        ns_cars, ns_wait = self.calculate_reward(ns)

        ew_cars, ew_wait = self.calculate_reward(ew)

        # make wait times be minimum 1
        # ns_wait += 1
        # ew_wait += 1

        if cur_action == LightAction.V_GREEN:
            tot = (self.pos_scale * (ns_wait) - self.neg_scale * (ew_cars * ew_wait))
            tot += self.buffer_scale * self.buffer_reward(buffer)
        elif cur_action == LightAction.H_GREEN:
            tot = (self.pos_scale * (ew_cars * ew_wait) - self.neg_scale * (ns_cars * ns_wait))
            tot += self.buffer_scale * self.buffer_reward(buffer)

        # elif cur_action == LightAction.H_YELLOW or cur_action == LightAction.V_YELLOW:
        #     tot = (1-act) * self.neg_scale * (-(ew_cars * ew_wait) - (ns_wait * ns_cars))
        else:
            tot = (1-act) * self.neg_scale * (-(ew_cars * ew_wait) - (ns_wait * ns_cars))

        return tot, (ns_wait + ew_wait) / 2

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

        return car_nums, stop_avg
