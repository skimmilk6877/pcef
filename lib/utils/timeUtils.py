#-*- coding: utf-8 -*-
# """
#
#
#
# """

import time

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
def timer(list):
    list.append(time.time())

def print_timer(list):
    print "time cost: %.2f s" % (list[len(list)-1] - list[len(list)-2])

def TimerAndPrint(list):
    timer(list)
    if len(list)>1: print_timer(list)