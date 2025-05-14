'''
    This is for a random player, when given a choice will choose one of the random options it has been given, and the game will play out like that.
    This is a class of an agent playing the game. 

    Attributes of the agent: 
        - Current Position in the game
        - Money  
        - Properties 
    
    Functions: 
        - Move forward 
        - Purchase Property 
        - Pay Rent 
        - Mortgage property          
'''

from utils import roll_dice
import random

class Player: 
    def __init__(self):
        self.money = 1500 ## $1500 USD as the starting money to each player in the beginning
        self.properties = []
        self.position = 0
        self.get_out_of_jail = 0
    
    def move_forward(self): 
        (d1,d2) = roll_dice()
        repeated = 0
        total = d1+d2
        if (d1==d2): 
            while(repeated < 3): 
                (d1,d2) = roll_dice()
                total += d1+d2
                if(d1==d2): 
                    repeated+=1 
                else: 
                    break
        
        if repeated == 3: 
            pos = "jail"
        else: 
            pos = pos+total

        return pos 

    def purchase_property(self): 
        pass 

    def pay_rent(self,property,agent): 
        rent = property.rent
        if self.money > rent: 
            agent.money += rent  
            self.money -= rent 
        else: 
            self.mortgage(rent)
        
    def mortgage(self,required_money): 
        ## Now what to morgage, is a decision of the agent - which would result in a "smart behaviour" --> Consider the property that is the being chosen is a random property, which should be greater than the rent that is paid
        money_got = 0
        chosen_mortgaged_properties = []
        while(required_money >= money_got): 
            
            ## Choose a property which is not already mortgaged. Keep choosing until you find one which is not, stop when you have choosen all the options. Do not choose a property more than once. 
            chosen = True
            properties = []
            while(chosen): 
                mortgaged_property = random.choice(self.properties)
                if not mortgaged_property.mortgaged: 
                    chosen = False
                    mortgaged_property.mortgaged = True
                else: 
                    if mortgaged_property not in properties: 
                        properties.append(mortgaged_property)
                
                if (len(properties) == len(self.properties)): 
                    self.bankrupt()
                    return False


            chosen_mortgaged_properties.append(random.choice(self.properties))
            money_got += chosen_mortgaged_properties.mortgage_value

    def bankrupt(): 
        print("The player is now bankrupted!!! Game over for them")
        ## Stop the execution here itself
        


            
            
            