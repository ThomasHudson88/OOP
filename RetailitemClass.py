#Create the retail item class
class Retailitem:

    #initialize the class
    def __init__(self, d, i, p):
        self.__description = d
        self.__unitsininventory = int(i)
        self.__price = float(p)


    def get_price(self):
        return self.__price
    
    def get_unitsinventory(self):
        return self.__unitsininventory
    
    def get_description(self):
        return self.__description