import random

class Insect:
    #Creating the insect Class

    def __init__(self):
        self.legs = 4
        self.wings = 2
        self.flight = 1

    def calcflight(self):
        self.flight = random.randint(1, 10)

    def get_miles(self):
            return self.flight

#created the class, then we initialize and then we give the flight the random number