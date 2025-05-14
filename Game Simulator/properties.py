'''
This contains the class of the all properties of the agent. 
We can have a class, for each individual property, and one class for the all the properties 

WHAT ARE THE PROPERTY TYPES AND THINGS IN MONOPOLY THAT I NEED TO KNOW 

Make 4x houses, cost of each? 
HOUSE

Cost of each hotel?
HOTEL 
# '''


# Purchase Price
# Mortgage Value
# Rent (No House)
# Rent (1 House)
# Rent (2 Houses)
# Rent (3 Houses)
# Rent (4 Houses)
# Rent (Hotel)

monopoly_properties = {
    "Mediterranean Avenue":   [60, 30, 2, 10, 30, 90, 160, 250, "Brown", 50],
    "Baltic Avenue":          [60, 30, 4, 20, 60, 180, 320, 450, "Brown", 50],
    "Oriental Avenue":        [100, 50, 6, 30, 90, 270, 400, 550, "Light Blue", 50],
    "Vermont Avenue":         [100, 50, 6, 30, 90, 270, 400, 550, "Light Blue", 50],
    "Connecticut Avenue":     [120, 60, 8, 40, 100, 300, 450, 600, "Light Blue", 50],
    "St. Charles Place":      [140, 70, 10, 50, 150, 450, 625, 750, "Pink", 100],
    "States Avenue":          [140, 70, 10, 50, 150, 450, 625, 750, "Pink", 100],
    "Virginia Avenue":        [160, 80, 12, 60, 180, 500, 700, 900, "Pink", 100],
    "St. James Place":        [180, 90, 14, 70, 200, 550, 750, 950, "Orange", 100],
    "Tennessee Avenue":       [180, 90, 14, 70, 200, 550, 750, 950, "Orange", 100],
    "New York Avenue":        [200, 100, 16, 80, 220, 600, 800, 1000, "Orange", 100],
    "Kentucky Avenue":        [220, 110, 18, 90, 250, 700, 875, 1050, "Red", 150],
    "Indiana Avenue":         [220, 110, 18, 90, 250, 700, 875, 1050, "Red", 150],
    "Illinois Avenue":        [240, 120, 20, 100, 300, 750, 925, 1100, "Red", 150],
    "Atlantic Avenue":        [260, 130, 22, 110, 330, 800, 975, 1150, "Yellow", 150],
    "Ventnor Avenue":         [260, 130, 22, 110, 330, 800, 975, 1150, "Yellow", 150],
    "Marvin Gardens":         [280, 140, 24, 120, 360, 850, 1025, 1200, "Yellow", 150],
    "Pacific Avenue":         [300, 150, 26, 130, 390, 900, 1100, 1275, "Green", 200],
    "North Carolina Avenue":  [300, 150, 26, 130, 390, 900, 1100, 1275, "Green", 200],
    "Pennsylvania Avenue":    [320, 160, 28, 150, 450, 1000, 1200, 1400, "Green", 200],
    "Park Place":             [350, 175, 35, 175, 500, 1100, 1300, 1500, "Dark Blue", 200],
    "Boardwalk":              [400, 200, 50, 200, 600, 1400, 1700, 2000, "Dark Blue", 200],
    # Railroads and Utilities (no house cost)
    "Short Line":             [200, 100, 25, 50, 100, 200,0,0,"Railroad"],
    "Reading Railroad":       [200, 100, 25, 50, 100, 200,0,0, "Railroad"],
    "Pennsylvania Railroad":  [200, 100, 25, 50, 100, 200,0,0, "Railroad"],
    "B. & O. Railroad":       [200, 100, 25, 50, 100, 200,0,0,"Railroad"],
    "Electric Company":       [150, 75, 4, 10,None, None, "Utility"],
    "Water Works":            [150, 75, 4, 10,None, None, "Utility"],
}


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

    '''
    def __init__(self): 
        self.properties_dict = monopoly_properties
        self.property = []
        # for i in self.properties_dict:
        #     self.properties_dict.append(Property(i,self.properties_dict[i]))
        #     self.make 
        
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

            
        






        
        