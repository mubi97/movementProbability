     # RandomWalk.py
#
# 10.2  Random Walk
#
# Introduction to Computational Science:  Modeling and Simulation for the Sciences
# Angela B. Shiflet and George W. Shiflet
# Wofford College
# Copyright 2006 by Princeton University Press
#

from graphics import *
from random import randrange
import time
import random

def decision(probability):
    return random.random() < probability


NE = 0
NW = 0
SE = 0
SW = 0

WIN_WIDTH  = 500
WIN_HEIGHT = 500

def main():
    
# Show the path and distance of last position from first

    # determine points of path
    x = x0 = 0
    y = y0 = 0
    n = 50  # number of steps
    xLst = [0] 
    yLst = [0] 
    lst = [[0, 0]]
    for i in range(n):
        decx = decision(0.3)
        decy = decision(0.45)
        if decx:
            x = x + 1
        else:
            x = x - 1
         
        if decy:
            y = y + 1
        else:
            y = y - 1

        xLst.append(x)
        yLst.append(y)
        lst.append([x, y])
    xmin = min(xLst)
    xmax = max(xLst)
    ymin = min(yLst)
    ymax = max(yLst)

    # display points in blue
    listPlot(xmin, ymin, xmax, ymax, lst)
       
    
# display points in blue with first and last point in red and
# lines segments connecting points

def listPlot(xmin, ymin, xmax, ymax, pts):
    global NE, NW, SE, SW
    win = GraphWin("Random Walk", WIN_WIDTH, WIN_HEIGHT)
    win.setBackground("white")
    win.setCoords(xmin - 1, ymin - 1, xmax + 1, ymax + 1)

    cir = Circle(Point(pts[0][0], pts[0][1]), 0.15)
    cir.setFill("red")
    cir.draw(win)
    ptPrev = pts[0]
    
    for pt in pts[1:]:
        line = Line(Point(ptPrev[0], ptPrev[1]), (Point(pt[0], pt[1])))
        line.draw(win)
        cir = Circle(Point(pt[0], pt[1]), 0.1)
        cir.setFill("blue")
        cir.draw(win)
        ptPrev = pt
        # time.sleep(0.3)


    cir = Circle(Point(pt[0], pt[1]), 0.15)
    cir.setFill("red")
    cir.draw(win)
    if (pt[1] > ymin):
        if (pt[0] > xmin):
            NE += 1
        else:
            NW += 1
    else:
        if (pt[0] > xmin):
            SE += 1
        else:
            SW += 1

for i in range(1000):
    main()

print("Ended in NE Quadrant " + str(NE) + " times")
print("Ended in NW Quadrant " + str(NW) + " times")
print("Ended in SE Quadrant " + str(SE) + " times")
print("Ended in SW Quadrant " + str(SW) + " times")
