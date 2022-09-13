# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:21:10 2022

@author: ts18jpf
"""

import random
import operator
import matplotlib.pyplot
import agentframework
import csv


environment = []
# Reading the file
with open("in.txt") as csvfile:
    dataset = csv.reader(csvfile, delimiter=',',quoting = csv.QUOTE_NONNUMERIC)
    # Loop for the rows
    for row in dataset:
        # Initialise the rowist
        rowlist = []
       
        # Loop for the values
        for value in row:
            rowlist.append(value)
            
        environment.append(rowlist)
        
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()       
    


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

agents.append(agentframework.Agent(0, 0))

agents.append(agentframework.Agent(environment))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(len(agents)):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

