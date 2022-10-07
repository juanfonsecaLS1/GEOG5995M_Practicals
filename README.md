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
| 01 Agent Based Modelling  | &nbsp;┣ 📜01A_Agent_based_modelling.py<br>&nbsp;┣ 📜01B_Randomise_100by100.py|
| 02 Code Shrinking I | &nbsp;┣📜03_ACode_Shrinking_II.py  |
| 03 Code Shrinking II  |&nbsp;┣📜03_BCode_Shrinking_II.py  |
| 04 Building Tools  |&nbsp;┣📜03_CTimingII.py |
| 05 Agents!<br />06 I/O|&nbsp;┣ 📂model<br />&nbsp;┃ ┣ 📜agentframework.py<br>&nbsp;┃ ┗ 📜model_v0.py|
| 07 Communicating  |&nbsp;┣ 📂model<br />&nbsp;┃ ┣ 📜agentframework.py<br>&nbsp;┃ ┗ 📜model.py |
| 08 Animation/Behaviour  |&nbsp;┣ 📂model_Animation<br />&nbsp;┃ ┣ 📜agentframework.py<br>&nbsp;┃ ┗ 📜model.py  |
| 09 GUI/WEB scrapping |&nbsp;┗ 📂model_GUI<br /> &nbsp; &nbsp; &nbsp;  ┣ 📜agentframework.py<br> &nbsp; &nbsp; &nbsp;  ┗ 📜model.py  |

## Agent Based Model
The ABM recreates the interaction of a specific number of individuals (agents) with each other and a defined environment. While all individuals move across a space limited by the size of the environment, their interaction with the environment consists of two actions, they can consume the environment's resources at a fixed rate; and, once their capacity is reached, deposit everything they have consumed. On the other hand, there is only one mechanism for interaction among individuals; they can share their resources with individuals located within a distance range.

The following sections describe the basic steps to open the Python files, set initial parameters, run the ABM, and obtain the outputs from the model.

### Requirements
The ABM was developed using Python 3.7 In order to be able to run it correctly the following modules should be available in the Python environment:
```
matplotlib
tkinter
random
csv
requests
bs4
```


### How to open it
#### Graphic User Interface (GUI)
##### Setting model parameters
##### Running the model 
#### Outputs
#### Limitations/Known Issues
