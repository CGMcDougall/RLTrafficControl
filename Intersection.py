import pygame as pg


class intersection:

    #temp intersection bullshit

    phase = 0

    def __init__(self, tp = 10.0):
        #temp
        self.timePhase = tp
        self.curTime = tp


    #Returns the phase of the light, (0 green, 1 = yellow, 2 = red) NW then SW
    def act(self,dt : float) -> int:
        self.curTime -= dt

        yellowDur = 2
        fullRed = 1

        if self.curTime < -self.timePhase:
            self.curTime = self.timePhase

        elif self.curTime < -self.timePhase + fullRed:
            return 2,2

        elif self.curTime < -self.timePhase + yellowDur + fullRed:
            return 2,1

        elif self.curTime < 0:
            return 2,0

        elif self.curTime < fullRed:
            return 2,2

        elif self.curTime < yellowDur + fullRed:
            return 1,2

        return 0,2