'''
This contains the class of the all properties of the agent. 
We can have a class, for each individual property, and one class for the all the properties 
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
    "Mediterranean Avenue":   [60, 30, 2, 10, 30, 90, 160, 250, "Brown"],
    "Baltic Avenue":          [60, 30, 4, 20, 60, 180, 320, 450, "Brown"],
    "Oriental Avenue":        [100, 50, 6, 30, 90, 270, 400, 550, "Light Blue"],
    "Vermont Avenue":         [100, 50, 6, 30, 90, 270, 400, 550, "Light Blue"],
    "Connecticut Avenue":     [120, 60, 8, 40, 100, 300, 450, 600, "Light Blue"],
    "St. Charles Place":      [140, 70, 10, 50, 150, 450, 625, 750, "Pink"],
    "States Avenue":          [140, 70, 10, 50, 150, 450, 625, 750, "Pink"],
    "Virginia Avenue":        [160, 80, 12, 60, 180, 500, 700, 900, "Pink"],
    "St. James Place":        [180, 90, 14, 70, 200, 550, 750, 950, "Orange"],
    "Tennessee Avenue":       [180, 90, 14, 70, 200, 550, 750, 950, "Orange"],
    "New York Avenue":        [200, 100, 16, 80, 220, 600, 800, 1000, "Orange"],
    "Kentucky Avenue":        [220, 110, 18, 90, 250, 700, 875, 1050, "Red"],
    "Indiana Avenue":         [220, 110, 18, 90, 250, 700, 875, 1050, "Red"],
    "Illinois Avenue":        [240, 120, 20, 100, 300, 750, 925, 1100, "Red"],
    "Atlantic Avenue":        [260, 130, 22, 110, 330, 800, 975, 1150, "Yellow"],
    "Ventnor Avenue":         [260, 130, 22, 110, 330, 800, 975, 1150, "Yellow"],
    "Marvin Gardens":         [280, 140, 24, 120, 360, 850, 1025, 1200, "Yellow"],
    "Pacific Avenue":         [300, 150, 26, 130, 390, 900, 1100, 1275, "Green"],
    "North Carolina Avenue":  [300, 150, 26, 130, 390, 900, 1100, 1275, "Green"],
    "Pennsylvania Avenue":    [320, 160, 28, 150, 450, 1000, 1200, 1400, "Green"],
    "Park Place":             [350, 175, 35, 175, 500, 1100, 1300, 1500, "Dark Blue"],
    "Boardwalk":              [400, 200, 50, 200, 600, 1400, 1700, 2000, "Dark Blue"],
    # Railroads: [Purchase Price, Mortgage, Rent (1 owned), Rent (2), Rent (3), Rent (4), Color]
    "Reading Railroad":       [200, 100, 25, 50, 100, 200, "Railroad"],
    "Pennsylvania Railroad":  [200, 100, 25, 50, 100, 200, "Railroad"],
    "B. & O. Railroad":       [200, 100, 25, 50, 100, 200, "Railroad"],
    "Short Line":             [200, 100, 25, 50, 100, 200, "Railroad"],
    # Utilities: [Purchase Price, Mortgage, Rent (1 owned multiplier), Rent (2 owned multiplier), Color]
    "Electric Company":       [150, 75, 4, 10, "Utility"],
    "Water Works":            [150, 75, 4, 10, "Utility"],
}



class Property: 
    def __init__(self,name,data):
        self.name = name
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
        self.sold = False
        self.owner = None 
        self.mortgaged = False 
    
    def get_rent(self): 
        pass

class Game_Properties:
    def __init__(self): 
        self.properties_dict = monopoly_properties
        self.property = []
        for i in self.properties_dict:
            self.properties_dict.append(Property(i,self.properties_dict[i]))
         




        
        