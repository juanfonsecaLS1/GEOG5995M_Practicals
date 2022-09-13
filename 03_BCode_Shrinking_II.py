# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:46:17 2022

@author: ts18jpf
"""

import random 
import operator as op
import matplotlib.pyplot
import time

start = time.process_time()

# Setting seed for reproducibility
random.seed(1)


'''
# Setting number of agents
num_of_iterations = 1
'''

def agent_process(num_of_agents = 100):
    # Creating an empty list
    agents = []
    
    
    # Creating a list of lists with the coordinates for num_of_agents
    for i in range(num_of_agents):
        agents.append([random.randint(0,100),random.randint(0,100)])
    
    #print(agents)
    
    '''
    # Moving all agents
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            # Changing x
            if (random.random() < 0.5):
                agents[i][0] = (agents[i][0] + 1) % 100
            else:
                agents[i][0] = (agents[i][0] - 1) % 100
                
           # Changing y
            if (random.random() < 0.5):
                agents[i][1] = (agents[i][1] + 1) % 100
            else:
                agents[i][1] = (agents[i][1] - 1) % 100
                
        #print(agents)
    '''
    
    # Calculating the distance between a pair of coordinates.
    def distance_between(agents_0,agents_1):    
        xd = (agents_0[0] - agents_1[0])**2
        yd = (agents_0[1] - agents_1[1])**2
        dist = (xd+yd)**0.5
        #print("dist", dist)
        return(dist)
    
    maxdist=0
    mindist=distance_between(agents[0], agents[num_of_agents-1])
    
    for i in range(num_of_agents):
        for j in range(i+1, num_of_agents):
            temp_dist = distance_between(agents[i], agents[j])
            if temp_dist > maxdist:
                maxdist = temp_dist
            if temp_dist < mindist:
                mindist = temp_dist
    #print(maxdist)
    end = time.process_time()
    
    # print("time = " + str(end - start)) 
                 
    
    '''
    # Definying the boundaries of the plot
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    
    # Producing a plot for all agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
    
    # Extracting the right, top, left and bottom most coordinates
    maxx = max(agents,key=op.itemgetter(0))
    maxy = max(agents,key=op.itemgetter(1))
    minx = min(agents,key=op.itemgetter(0))
    miny = min(agents,key=op.itemgetter(1))
    
    # Plotting the extrame coordinates with specific colours
    matplotlib.pyplot.scatter(maxx[0],maxx[1],color = 'red')
    matplotlib.pyplot.scatter(maxy[0],maxy[1],color = 'pink')
    matplotlib.pyplot.scatter(minx[0],minx[1],color = 'black')
    matplotlib.pyplot.scatter(miny[0],miny[1],color = 'yellow')
    
    # Producing the plot
    matplotlib.pyplot.show()
    '''
    return(end - start)

for i in range(1,100):
    matplotlib.pyplot.scatter(i,agent_process(i))

matplotlib.pyplot.show()


