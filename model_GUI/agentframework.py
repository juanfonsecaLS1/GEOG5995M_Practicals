# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:31:53 2022

@author: ts18jpf
"""
import random



class Agent():
    
    # Defines the class and defines x and y as optional arguments
    def __init__ (self, environment, agents, cmap, x = None, y = None):
        """
        Definition of the class
        
        Parameters
        ----------
        environment : list
            List of list with rasted data of 'available resources' in the environment.
        agents : list
            List of agents
        cmap : colormap
            Base colormap which is used to define colours for plots.
        x : int, optional
            x coordinate of a given agent. The default is None.
        y : int, optional
            y coordinate of a given agent. The default is None.

        Returns
        -------
        None.

        """
        self.environment = environment
        self.store = 0
        self.agents = agents
        self.colour = cmap(random.random())
        
        
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
            
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) +((self.y - agent.y)**2))**0.5

    def share_with_neighbours(self,neighbourhood):
        # Loop through the agents in self.agents .
        for i in range(len(self.agents)):
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(self.agents[i])
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # print('Sharing!') #Added to test the if statement
                # Sum self.store and agent.store .
                totalstore=self.store + self.agents[i].store
                # Divide sum by two to calculate average.
                avgstore = totalstore/2
                # self.store = average
                self.store = avgstore
                # agent.store = average
                self.agents[1].store = avgstore
                # print("sharing: " + str(avgstore) + ", distance: " + str(distance))
    # End if
# End loop
        

