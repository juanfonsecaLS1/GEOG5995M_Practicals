# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:31:53 2022

@author: ts18jpf
"""
import random

class Agent():
    
    # Defines the class and defines x and y as optional arguments
    def __init__ (self, environment, x = None, y = None):
        self.environment = environment
        self.store = 0
        
        # Define the limits for randomising
        n_rows = len(self.environment)
        n_values = len(self.environment[0])
        
        if x == None:
            self._x = random.randint(0, n_values)
            # print('x is randomised as it was not provided')
        else:
            self._x = x
            
        if y == None:
            self._y = random.randint(0, n_rows)
            # print('y is randomised as it was not provided')
        else:
            self._y = y
        
    
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
            self._x = (self._x + 1) % len(self.environment[len(self.environment)-1])
        else:
            self._x = (self._x - 1) % len(self.environment[len(self.environment)-1])
        
        if (random.random() < 0.5):
            self._y = (self._y + 1) % len(self.environment)
        else:
            self._y = (self._y - 1) % len(self.environment)

    def eat(self):
        # For eating
        if self.environment[self.y][self.x] > 9: 
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        
        # For sicking up the store if >100
        if self.store > 100: 
            self.environment[self.y][self.x] += self.store
            self.store = 0
        

