# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:31:53 2022

@author: ts18jpf
"""
import random

class Agent():
    
    # Defines the class and defines x and y as optional arguments
    def __init__ (self, x = None, y = None):
        if x == None:
            self._x = random.randint(0, 99)
        else:
            self._x = x
            
        if y == None:
            self._y = random.randint(0, 99)
        else:
            self._y = y
    
    @property
    def x (self):
        return(self._x)
    
    @property
    def y (self):
        return(self._y)
            
    def move (self):
        # Changing x
        if (random.random() < 0.5):
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
        
        if (random.random() < 0.5):
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
           