import numpy as np
import Matricies as mat
import random

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
    def calculate_reward(array):
        stop_avg = 0.0
        car_nums = 0

        #loop over each array and average the stoptime and also count # of cars in array 
        for car in array: 
            car_nums += 1
            stop_avg += car.stoptime 
        
        stop_avg = stop_avg/car_nums

        return car_nums, stop_avg