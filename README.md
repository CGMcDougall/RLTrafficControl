# RLTrafficControl

## Authors:
Larina Aribi - 101185799 larinaaribi@cmail.carleton.ca <br/>
Sean Le - 101184583 seanle@cmail.carleton.ca <br/>
Annie Zhang - 101187995 anniezhang3@cmail.carleton.ca <br/>
Connor McDougall - 101179300 connormcdougall@cmail.carleton.ca <br/>


## Problem statement: Traffic Control
This project will deal with controlling the traffic lights at a four-way intersection by determining the most optimal time intervals based on incoming traffic. <br/> 
As this is a problem that has been optimized from a large number of different angles, we hope to bring our own take on it by combining other approaches to hopefully create a result that is more practical and realistic.

## Feasibility: 
Reinforcement learning is a suitable approach to this project because it has a very small set of possible actions at any given point, but the complexity of the state can be very high. The base set of actions would simply be to change the North/South lights from red to green or vice versa, and keeping the West/East lights the opposite. Though complexity could be added by factoring in turning lights. Some environmental factors we could potentially consider might be time of day, pedestrian traffic, main roads vs side roads, etc. The complexity of the environment can easily be scaled to fit the scope of the project.

## Setup:
Requires Pyhton, pygame, Pipx, and Copier. 
For Setting up Pipx and Copier, I ran the following (Windows): <br>

**Setup Scoop, Windows powershell Installer:**
1. *Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser*
2. *Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression* <br>

**Install Pipx using scoop, and setup path:**

3. *scoop install pipx*
4. *pipx ensurepath* <br>

**Install Copier using pipx:**

5. *pip install copier* <br>