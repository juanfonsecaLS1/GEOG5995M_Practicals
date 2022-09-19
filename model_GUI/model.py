# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 13:21:10 2022

@author: ts18jpf
"""
# Importing modules and packages
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import random
import matplotlib.pyplot
import matplotlib.animation 
import matplotlib.cm as cm
import csv
import requests
import bs4
# This imports the module with the class and methods definition for the ABM
import agentframework

# random.seed(1) # Used only when testing to obtain consistent results

num_of_agents = 0
num_of_iterations = 0
neighbourhood = 0

agents = []
environment = []

# This extracts a specific colourmap for assigning colours to each agent
cmap = cm.get_cmap('jet')

fig = matplotlib.pyplot.figure(figsize = [8,8])

def set_pars():
    """
    # This function assigns values to the parameters for the ABM run

    Default values are assigned if the values in the input boxes are not valid
    or missing.
    
    Returns
    -------
    None.

    """
    global num_of_agents
    global num_of_iterations
    global neighbourhood
    global ready

    # Exceptions declaration for wrong/missing values
    try:
        num_of_agents = int(in_nag.get())
    except ValueError :
        num_of_agents = 20
        in_nag.delete(0,tkinter.END)
        in_nag.insert(0,"20")

    try:
        num_of_iterations = int(in_it.get())
    except ValueError :
        num_of_iterations = 1000
        in_it.delete(0,tkinter.END)
        in_it.insert(0,"1000")
    try:
        neighbourhood = int(in_nei.get())
    except ValueError :
        neighbourhood = 40
        in_nei.delete(0,tkinter.END)
        in_nei.insert(0,"40")

    # Activates the Menu option for running the model
    model_menu.entryconfig("Run model", state = "normal")
    
    # Runs the initial processes
    initial()
    
    # Disables the set parameters button and entry widgets to avoid errors
    setButton.config(state = "disabled")
    in_nag.config(state = "disabled")
    in_it.config(state = "disabled")
    in_nei.config(state = "disabled")
    
    # Produces a notification for the user of the GUI 
    lbl0.config(text = "Parameters loaded! Run model using the menu")
    



def initial():
    """
    Function that runs all the initial processes:
        - Loading the web data with the initial values of x and y coordinates
        - Reading the text file with the environment data
        - Creating the list of agents based on the initial parameters set in the function set_pars

    Returns
    -------
    None.

    """
    
    # Declaration of the global variables that are going to be assigned within the functions
    global environment
    global agents
    
        
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
    
    
    # Extract the x and y data when available
    for i in range(num_of_agents):
        try:
            y = int(td_ys[i].text)
            x = int(td_xs[i].text)
        except:
            y = None
            x = None
        
        agents.append(agentframework.Agent(environment,agents,cmap, x = x, y = y))
    
    
def update(frame_number):
    """
    This function produces a plot with the agents and the current environment.
    Colour scale is fixed to make all frames consistent
    Size of the agents are proportional to the current store
    Alpha is modified for visualisation purposes
    
    
    Parameters
    ----------
    frame_number : int (automatically provided by the animation function)
        

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
    matplotlib.pyplot.imshow(environment, vmin=0, vmax=400, cmap='YlGn', aspect='auto')

    for i in range(num_of_agents):
        
        if agents[i].store < 1:
            a = 1
        else:
            a = (1/(agents[i].store**0.2))
        
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, s = agents[i].store*5, c = [agents[i].colour], alpha = a)

def outputs():
    """
    This function produces two text files in CSV format:
        - FinalEnvironment.txt contains the environment raster data after the run
        - AgentStorage.txt contains the record of the final store of all agents for each run

    Returns
    -------
    None.

    """
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

def run():
    """
    This function produces the animated plot in the canvas area with an specific number of iterations

    Returns
    -------
    None.

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
    canvas.draw()
    # print(num_of_iterations) #Added for testing purposes
    outputs()

# Ensuring a clean end of the main tkinter loop when closing window
def on_closing():
    root.quit()

# This specifies the GUI using tkinter
root = tkinter.Tk()
root.wm_title("Agent Based Model")
menu_bar = tkinter.Menu(root)

root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.entryconfig("Run model", state="disabled") 

# Setting up all input boxes, labels and buttons
lbl0 = tkinter.Label(root, text = "Type the model parameters (Default values are used if none or invalid)")
lbl0.grid(row=0, column=0, columnspan=7)

lbl1 = tkinter.Label(root, text = "Number of agents ->")
lbl1.grid(row=1, column=0)

in_nag = tkinter.Entry(root)
in_nag.grid(row=1, column=1)

lbl2 = tkinter.Label(root, text = "Neighbourhood ->")
lbl2.grid(row=1, column=2)

in_nei = tkinter.Entry(root)
in_nei.grid(row=1, column=3)

lbl3 = tkinter.Label(root, text = "Iterations ->")
lbl3.grid(row=1, column=4)

in_it = tkinter.Entry(root)
in_it.grid(row=1, column=5)

setButton = tkinter.Button(root, text="Set parameters", command=set_pars)
setButton.grid(row=1, column=6)

# Defines the canvas area that is going to take the animated plot
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.grid(row=2, column=0, columnspan=7)

# Triggers the on_closing method when the window is closed
root.protocol("WM_DELETE_WINDOW", on_closing)
tkinter.mainloop()



