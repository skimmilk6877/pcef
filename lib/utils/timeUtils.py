#-*- coding: utf-8 -*-
# """
#
#
#
# """

import time

class TimeUtils():

    TIMER_LIST = None

    def __init__(self):
        self.TIMER_LIST = []

    def clear(self):
        self.TIMER_LIST = []

    def timer(self):
        self.TIMER_LIST.append(time.time())
    def getTimerDifference(self,pointA,ponitB):
        return  (self.TIMER_LIST[pointA]-self.TIMER_LIST[ponitB])

    def print_timer(self):
        print "time cost: %.2f s" % self.getTimerDifference(-1,-2)

    def timerAndPrint(self):
        self.timer()
        if len(self.TIMER_LIST)>1: self.print_timer()
    def printTotalTime(self):

        if len(self.TIMER_LIST) > 1 : print 'total time %.2f s' % self.getTimerDifference(-1,0)

#usage:
#Initialize list timer
#TIMER_LIST=[]
#Place in all the places you want to record time
#only Record the difference between the two points.
#TimerAndPrint(TIMER_LIST)
#
#
#
#
