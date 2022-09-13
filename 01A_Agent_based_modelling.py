# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:53:43 2022

@author: ts18jpf
"""
import random
random.seed()

# Make a y variable.
x0 = 50

# Make a x variable.
y0 = 50

print("x0", x0)
print("y0", y0)

# Change y and x based on random numbers.
x = random.random()
if (x<0.5):
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)

# Move 
x = random.random()
if (x<0.5):
    y0 = y0 + 1
else:
    y0 = y0 - 1    
print("y0", y0)


    

# Make a second set of y and xs, and make these change randomly as well.

# Make a y variable.
x1 = 50

# Make a x variable.
y1 = 50

x = random.random()
if (x<0.5):
    x1 = x1 + 1
else:
    x1 = x1 - 1
  
print("x1", x0)

x = random.random()
if (x<0.5):
    y1 = y1 + 1
else:
    y1 = y1 - 1    
print("y1", y0)

# Work out the distance between the two sets of y and xs.
xd = (x0 - x1)**2
print("xd", xd)

yd = (y0 - y1)**2
print("yd", yd)

dist = (xd+yd)**0.5
print("dist", dist)