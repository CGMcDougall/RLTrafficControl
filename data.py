import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Data:

    WaitTime = [[]]
    meanTime =0
    n = 0


    def __init__(self):
        return


    def addToQueue(self,x,time):
        print((time))
        try:
            self.WaitTime[int(math.floor(time))].append(x)
        except:
            self.WaitTime.append([x])

        self.meanTime = ((self.n * self.meanTime) + x) / (self.n + 1)
        self.n += 1



    def plot(self):

        print(self.WaitTime)


        # Step 1: Flatten the matrix into x, y coordinates
        x = []
        y = []

        for i, sublist in enumerate(self.WaitTime):
            for j, value in enumerate(sublist):
                x.append(i)  # x-coordinate is the sublist index
                y.append(value)  # y-coordinate is the value from the sublist


        plt.figure(figsize=(10, 6))
        #plt.scatter(x, y,c=y)
        plt.scatter(x, y)

        plt.ylabel('Car Wait Time')
        plt.xlabel('Time')
        plt.title('Scatter Plot WaitTime')
        plt.autumn()

        plt.show()













