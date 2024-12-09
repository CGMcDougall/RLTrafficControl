import math
import matplotlib.pyplot as plt
import numpy as np

class Data:

    WaitTime = [[]]
    meanTime =0
    n = 0


    def __init__(self):
        return


    # x = total wait time of a car
    # time = the time in which it happened (time step?)
    def addToQueue(self,x,time):
        #print((x))
        try:
            self.WaitTime[int(math.floor(time))].append(x)
        except:
            self.WaitTime.append([x])

        self.meanTime = ((self.n * self.meanTime) + x) / (self.n + 1)
        self.n += 1



    def plot(self):

        #print(self.WaitTime)


        # Step 1: Flatten the matrix into x, y coordinates
        x = []
        y = []

        for i, sublist in enumerate(self.WaitTime):
            for j, value in enumerate(sublist):
                x.append(i)  # x-coordinate is the sublist index
                y.append(value)  # y-coordinate is the value from the sublist


        plt.figure(figsize=(10, 6))
        #plt.scatter(x[2000:], y[2000:],c=y[2000:])


        # fit = np.polyfit(x[25000:], y[25000:], 1)
        # fit_fn = np.poly1d(fit)

        plt.scatter(x, y)

        #plt.scatter(x[25000:], fit_fn(x[25000:]))  # orange

        plt.grid()
        plt.ylabel('Average Car Wait Time')
        plt.xlabel('Time (In Frames)')
        plt.title('Model')
        plt.autumn()



        plt.show()




