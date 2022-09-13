# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 13:45:31 2022

This is to solve:
    You actually have everything you need to know in order to randomly start the coordinates
    at different locations. See if you can randomise their starting points within a 100x100 grid,
    with the coordinates being integer values between and including 0 and 99 (if you look back
    over the practical you'll see we mention an appropriate function). Once you've managed that,
    comment your code so you'll understand it later, and you're done.
    
@author: ts18jpf
"""

import random

# Definying variables for time 0
x0=random.randint(0,99)
print("x0",x0)

y0=random.randint(0,99)
print("y0",y0)


# Definying variables for time 1
x1=random.randint(0,99)
print("x1",x1)

y1=random.randint(0,99)
print("y1",y1)


# Work out the distance between the two sets of y and xs.
xd = (x0 - x1)**2
print("xd", xd**0.5)

yd = (y0 - y1)**2
print("yd", yd**0.5)


dist = (xd+yd)**0.5
print("dist", dist)



