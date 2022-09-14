# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:31:53 2022

@author: ts18jpf
"""
import random

class Agent():
    
    # Defines the class and defines x and y as optional arguments
    def __init__ (self, environment, x = None, y = None):
        if x == None:
            self._x = random.randint(0, 99)
            # print('x is randomised as it was not provided')
        else:
            self._x = x
            
        if y == None:
            self._y = random.randint(0, 99)
            # print('y is randomised as it was not provided')
        else:
            self._y = y
        self.environment = environment
        self.store = 0
    
    def __str__ (self):
        return (f'Agent located in x: {self._x}, y: {self._y}, stores: {self.store}')
        #return print(f"Agent({self._x},{self._y},{self.store})")
    
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

    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 0: 
            self.environment[self.y][self.x] -= 10
            self.store += 10

