'''
This is the main game simulator for Monopoly. All the objects and the controls will be here
Given the simulator, we have a state space that needs to be moved

Utils: 
- Dice (2 dice, 1-6 - total will be used as the next move)
- Make 

Elements: 
- Player 
- Bank 
- Community Cards
- Chance Cards 

Game: 
- State (Properties and their orders)
- 

The most basic version: 
    - Agents should be able to move their pieces
    - Agents should be able to purchase the properties 
    - Agents should be able to give and take rent in case one lands on someone else's property 
    - In case the agent is unable to make a transactions (purchase propertly, give rent etc.) he can mortgage the property in order carry out the expense 
    - The agent could deny to purchase a propertly 
'''

from utils import roll_dice
