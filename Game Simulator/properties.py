from utils import board_extras

'''
This contains the class of the all properties of the agent. 
We can have a class, for each individual property, and one class for the all the properties 

WHAT ARE THE PROPERTY TYPES AND THINGS IN MONOPOLY THAT I NEED TO KNOW 

Make 4x houses, cost of each? 
HOUSE

Cost of each hotel?
HOTEL 
# '''

def go():
    pass

def community_chest():
    pass

def income_tax(amount):
    pass

def chance():
    pass

def jail():
    pass

def electric_company():
    pass

def free_parking():
    pass

def water_works():
    pass

def go_to_jail():
    pass

def luxury_tax(amount):
    pass



# Purchase Price
# Mortgage Value
# Rent (No House)
# Rent (1 House)
# Rent (2 Houses)
# Rent (3 Houses)
# Rent (4 Houses)
# Rent (Hotel)

monopoly_board = {
    0: go(),  # Go
    1: ["Mediterranean Avenue",   [60, 30, 2, 10, 30, 90, 160, 250, "Brown", 50]],
    2: community_chest(),
    3: ["Baltic Avenue",          [60, 30, 4, 20, 60, 180, 320, 450, "Brown", 50]],
    4: income_tax(200),
    5: ["Reading Railroad",       [200, 100, 25, 50, 100, 200, 0, 0, "Railroad"]],
    6: ["Oriental Avenue",        [100, 50, 6, 30, 90, 270, 400, 550, "Light Blue", 50]],
    7: chance(),
    8: ["Vermont Avenue",         [100, 50, 6, 30, 90, 270, 400, 550, "Light Blue", 50]],
    9: ["Connecticut Avenue",     [120, 60, 8, 40, 100, 300, 450, 600, "Light Blue", 50]],
    10: jail(),
    11: ["St. Charles Place",     [140, 70, 10, 50, 150, 450, 625, 750, "Pink", 100]],
    12: electric_company(),
    13: ["States Avenue",         [140, 70, 10, 50, 150, 450, 625, 750, "Pink", 100]],
    14: ["Virginia Avenue",       [160, 80, 12, 60, 180, 500, 700, 900, "Pink", 100]],
    15: ["Pennsylvania Railroad", [200, 100, 25, 50, 100, 200, 0, 0, "Railroad"]],
    16: ["St. James Place",       [180, 90, 14, 70, 200, 550, 750, 950, "Orange", 100]],
    17: community_chest(),
    18: ["Tennessee Avenue",      [180, 90, 14, 70, 200, 550, 750, 950, "Orange", 100]],
    19: ["New York Avenue",       [200, 100, 16, 80, 220, 600, 800, 1000, "Orange", 100]],
    20: free_parking(),
    21: ["Kentucky Avenue",       [220, 110, 18, 90, 250, 700, 875, 1050, "Red", 150]],
    22: chance(),
    23: ["Indiana Avenue",        [220, 110, 18, 90, 250, 700, 875, 1050, "Red", 150]],
    24: ["Illinois Avenue",       [240, 120, 20, 100, 300, 750, 925, 1100, "Red", 150]],
    25: ["B. & O. Railroad",      [200, 100, 25, 50, 100, 200, 0, 0, "Railroad"]],
    26: ["Atlantic Avenue",       [260, 130, 22, 110, 330, 800, 975, 1150, "Yellow", 150]],
    27: ["Ventnor Avenue",        [260, 130, 22, 110, 330, 800, 975, 1150, "Yellow", 150]],
    28: water_works(),
    29: ["Marvin Gardens",        [280, 140, 24, 120, 360, 850, 1025, 1200, "Yellow", 150]],
    30: go_to_jail(),
    31: ["Pacific Avenue",        [300, 150, 26, 130, 390, 900, 1100, 1275, "Green", 200]],
    32: ["North Carolina Avenue", [300, 150, 26, 130, 390, 900, 1100, 1275, "Green", 200]],
    33: community_chest(),
    34: ["Pennsylvania Avenue",   [320, 160, 28, 150, 450, 1000, 1200, 1400, "Green", 200]],
    35: ["Short Line",            [200, 100, 25, 50, 100, 200, 0, 0, "Railroad"]],
    36: chance(),
    37: ["Park Place",            [350, 175, 35, 175, 500, 1100, 1300, 1500, "Dark Blue", 200]],
    38: luxury_tax(100),
    39: ["Boardwalk",             [400, 200, 50, 200, 600, 1400, 1700, 2000, "Dark Blue", 200]],
}


exception_cells = [
    0,   # go()
    2,   # community_chest()
    4,   # income_tax()
    7,   # chance()
    10,  # jail()
    12,  # electric_company()
    17,  # community_chest()
    20,  # free_parking()
    22,  # chance()
    28,  # water_works()
    30,  # go_to_jail()
    33,  # community_chest()
    36,  # chance()
    38   # luxury_tax()
]


class Property: 
    def __init__(self,owner,data):
        self.owner = owner ## This is the Owner (Agent) object, which is passed as parameter here
        self.houses = 0
        self.hotel = 0
        self.mortgage_value = data[0]
        self.rent = data[1]
        self.rent_1 = data[2]
        self.rent_2 = data[3]
        self.rent_3 = data[4]
        self.rent_4 = data[5]
        self.rent_hotel = data[6]
        self.color = data[7]
        self.category = data[8]
        self.sold = False
        self.owner = None 
        self.mortgaged = False 
    
    def get_rent(self): 
        '''
        '''
        pass

class Game_Properties:
    '''
    This class stores all the game properties objects sequentially
    Central place to get access to a particular object here 

    
    All the cells are represented in a linear way numbered from 1 - 40 
    It is a dictionary, in which each number corresponds to respective property object. 
    '''
    def __init__(self): 
        self.properties_dict = {}
        self.init_properties()
        self.property = []
        # for i in self.properties_dict:
        #     self.properties_dict.append(Property(i,self.properties_dict[i]))
        #     self.make 
        
    def init_properties(self): 
        '''
        This creates objects for the different properties and stores sequentially in a dictionary
        Cells 0 (Go) - 39(Broadwork)
        40 cells   

        Special cells: 

        0: Go (200)
        10: Jail 
        20: Free Parking 
        30: Go to Jail 

        Tax:
        4:  Income Tax ($200)
        38: Luxury Tax ($100)

        Community Chest: 
        2
        17
        33

        Chance: 
        7
        22 
        36
    
        Utils: 
        12: Electric Company 
        28: Water Works 
        '''
        dict_iter = iter(monopoly_properties)
        for i in range(0,41): 
            key = next(dict_iter)
            if i not in exception_cells: 
                self.properties_dict[i] = Property(key,monopoly_properties[key])
            else:
                self.properties_dict[i] = monopoly_properties[key]

                

    def take_rent(self,property,agent_landed): 
        '''
            Inputs (Objects): Property, Agent Landed (Agent)
        '''
        owner = property.owner ##The owner object

        rent = property.rent
        if agent_landed.money > rent:
            owner.money += rent 
            agent_landed.money -= rent
        else:
            agent_landed.mortgage(rent) ## Need to add this, should be a characteristic of the agent, not the property - as they will not necessarily mortgate this property.
            self.take_rent(property,agent_landed)

            
        






        
        