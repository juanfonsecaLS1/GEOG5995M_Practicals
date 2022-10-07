# GOEG5995M - First assignment
This portfolio contains the code produced for the GEOG5995M module. The scripts in this repository evidence
the different stages of the development of the final [Agent Based Model](#agent-based-model). 


## Contents
<details>
  <summary>Expand table of contents</summary>
  
  1. [Repository Structure](#repository-structure)
  2. [Agent Based Model](#agent-based-model)
      1. [Requirements](#requirements)
      1. [How to open it](#how-to-open-it)
      2. [Graphic User Interface](#graphic-user-interface-gui)
      3. [Outputs](#outputs)
      4. [Limitations and Known Issues](#limitationsknown-issues)
</details>

## Repository Structure
The following table shows the correspondence of the files and the different practicals. Comments have been added to describe the code in blocks as appropiated. In some cases, lines used for testing purposes have also been commented to avoid the execution while running the code.    

|  Practical | Associated File(s) in the<br> 📦Repository|
| :------------ | :------------ |
| 01 Agent Based Modelling  | &nbsp;┣📜01A_Agent_based_modelling.py<br>&nbsp;┣📜01B_Randomise_100by100.py|
| 02 Code Shrinking I | &nbsp;┣📜03_ACode_Shrinking_II.py  |
| 03 Code Shrinking II  |&nbsp;┣📜03_BCode_Shrinking_II.py  |
| 04 Building Tools  |&nbsp;┣📜03_CTimingII.py |
| 05 Agents!<br />06 I/O|&nbsp;┣ 📂model<br />&nbsp;┃ ┣📜agentframework.py<br>&nbsp;┃ ┗📜model_v0.py|
| 07 Communicating  |&nbsp;┣ 📂model<br />&nbsp;┃ ┣📜agentframework.py<br>&nbsp;┃ ┗📜model.py |
| 08 Animation/Behaviour  |&nbsp;┣ 📂model_Animation<br />&nbsp;┃ ┣📜agentframework.py<br>&nbsp;┃ ┗📜model.py  |
| 09 GUI/WEB scrapping |&nbsp;┗ 📂model_GUI<br /> &nbsp; &nbsp; &nbsp;  ┣📜agentframework.py<br> &nbsp; &nbsp; &nbsp;  ┗📜model.py  |

## Agent Based Model
The ABM recreates the interaction of a specific number of individuals (agents) with each other and a defined environment. While all individuals move across a space limited by the size of the environment, their interaction with the environment consists of two actions, they can consume the environment's resources at a fixed rate; and, once their capacity is reached, deposit everything they have consumed. On the other hand, there is only one mechanism for interaction among individuals; they can share their resources with individuals located within a distance range.

The following sections describe the basic steps to open the Python files, set initial parameters, run the ABM, and obtain the outputs from the model.

### Requirements
The ABM was developed using the Anaconda distribution with Python 3.7. In order to be able to run it correctly the following modules should be available in the Python environment:
```
matplotlib
tkinter
random
csv
requests
bs4
```
### How to open it
The files can be opened and run using a Python IDE such as Spyder or calling the model from the Anaconda command prompt. The second method requires less steps and, therefore, is less likely to fail. The steps are: 
1. Save the model files in your local drive
2. In the Anaconda command prompt, change the working directory to the directory where the files are saved. For example:
```
cd /d M:\MSc\GOEG5995M\01_practical_agent_based\model_GUI
```
3. Run the main file of the model using the command
```
python model.py
```
After a few seconds, the a window will appear.
#### Graphic User Interface (GUI)
The GUI allows the user to the model parameters and run the model.
##### Setting model parameters
Three parameters can be specified using integers:
- the __*Number of agents*__ in the simulation
- the distance threshold used to determine when the agents share their resources i.e. are in the same __*Neighbourhood*__
- the maximun __*Number of iterations*__ to be produced

![Clean Parameters](https://user-images.githubusercontent.com/69847296/194627694-23edeb5c-db51-407c-8bd5-2ac52dd2d33a.png)

Once the parameters are defined, they can be set using the button on the top right. If one or more parameters are invalid or missing, default values are used. 
##### Running the model 
To run the model, click on *Model >> Run Model*. 

![Run model](https://user-images.githubusercontent.com/69847296/194627955-f54ab3f9-c851-4748-a840-3a810e81b582.png)

The window will show an animation with all iterations. In the plot, resources in each location are shown using a colour scale, and the size of the agents indicate the current amount of store.

![model_visual](https://user-images.githubusercontent.com/69847296/194628069-5c8e89be-f9e1-4258-a7a4-3caaa5282367.png)

#### Outputs
Once the model has stopped, two outputs are produced in the same working directory.
- ```FinalEnvironment.txt``` saves the status of the environment after the selected number of iterations
- Each line in ```AgentStorage.txt``` corresponds to the amount stored by all agents at the end of a single run of the model.
#### Limitations/Known Issues
