import random

class Insect:
    #Creating the insect Class

    def __init__(self,w,l,n):
        self.wings = w
        self.legs = l
        self.flight = 0
        self.name = n


    def calcflight(self):
        self.flight = random.randint(1, 10)
        #get methods and accesor methods, some change a value and others just get the vlaue
        #we have these seperate because they serve a specific func

    def get_miles(self):
            return self.flight
    
    def get_name(self):
            return self.name

#created the class, then we initialize and then we give the flight the random number
#Always have to __init__ and list all the attributes
