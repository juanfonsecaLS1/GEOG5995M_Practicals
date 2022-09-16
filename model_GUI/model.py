# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:21:10 2022

@author: ts18jpf
"""
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import random
import matplotlib.pyplot
import matplotlib.animation 
import matplotlib.cm as cm
import agentframework
import csv
import requests
import bs4


#import sys

random.seed(1)

# %matplotlib qt

num_of_agents = 20
num_of_iterations = 1000
neighbourhood = 40

agents = []
environment = []

stop_plot = False

cmap = cm.get_cmap('jet')

fig = matplotlib.pyplot.figure(figsize = [8,8])

def set_pars():
    global num_of_agents
    global num_of_iterations
    global neighbourhood

    
    try:
         num_of_agents = int(in_nag.get())
    except ValueError :
        num_of_agents = 20

    try:
        num_of_iterations = int(in_it.get())
    except ValueError :
        num_of_iterations = 1000
        
    try:
        neighbourhood = int(in_nei.get())
    except ValueError :
        neighbourhood = 40
        
    initial()
    run()
    



def initial():
    global environment
    global agents
    
    agents = []
    environment = []
    
    r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify = False)
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class" : "y"})
    td_xs = soup.find_all(attrs={"class" : "x"})
    
    
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
    
    
    # Make the agents.
    for i in range(num_of_agents):
        try:
            y = int(td_ys[i].text)
            x = int(td_xs[i].text)
        except:
            y = None
            x = None
        
        agents.append(agentframework.Agent(environment,agents,cmap, x = x, y = y))
    
    
# Move the agents.
def update(frame_number):
    """

    Parameters
    ----------
    frame_number : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    fig.clear()
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

    matplotlib.pyplot.xlim(0, len(environment[0]))
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.imshow(environment, vmin=0, vmax=400, cmap='PuBuGn', aspect='auto')

    for i in range(num_of_agents):
        
        if agents[i].store < 1:
            a = 1
        else:
            a = (1/(agents[i].store**0.2))
        
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, s = agents[i].store*5, c = [agents[i].colour], alpha = a)

def run():
    initial()
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    canvas.draw()
    print(num_of_iterations)
    

root = tkinter.Tk()
root.wm_title("Agent Based Model")
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

lbl1 = tkinter.Label(root, text = "Number of agents ->")
lbl1.grid(row=0, column=0)

in_nag = tkinter.Entry(root)
in_nag.grid(row=0, column=1)

lbl2 = tkinter.Label(root, text = "Neighbourhood ->")
lbl2.grid(row=0, column=2)

in_nei = tkinter.Entry(root)
in_nei.grid(row=0, column=3)

lbl3 = tkinter.Label(root, text = "Iterations ->")
lbl3.grid(row=0, column=4)

in_it = tkinter.Entry(root)
in_it.grid(row=0, column=5)

setButton = tkinter.Button(root, text="Set parameters", command=set_pars)
setButton.grid(row=0, column=6)

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.grid(row=1, column=0, columnspan=7)

tkinter.mainloop()

'''
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
