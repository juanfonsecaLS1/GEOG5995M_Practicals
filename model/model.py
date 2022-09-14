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
# Reading the environment file
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
      
num_of_agents = 20
num_of_iterations = 10000
neighbourhood = 50 

agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))

# agents.append(agentframework.Agent(environment,x = 1,y = 1)) # This is to test if an agent is correctly positioned

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


# Writing the environment at the end
f = open("FinalEnvironment.txt", 'w+',   newline = "")
with f:
    write = csv.writer(f) 
    write.writerows(environment)
f.close()

# Writing the Agent storage, a+ argument is used to append the files
f_store = open("AgentStorage.txt", 'a+',   newline = "")
tmp_store=[]
with f_store:
    write = csv.writer(f_store)
    tmp_store=[]
    for k in range(num_of_agents):
        tmp_store.append(agents[k].store)
    #print(tmp_store) # Print for testing the result of the storage in each iteration
    write.writerow(tmp_store)
f_store.close()


'''
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
'''