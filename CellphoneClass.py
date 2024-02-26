import random

#Create a phone class
class CellPhone:

    def __init__(self, m, n, p):
        self.__manufact = m
        self.__model = n
        self.__retail_price = p
    
    def set_manufact(self,m):
        self.__manufact = m

    def get_manufact(self,m):
        return self.__manufact

    def set_model(self,m):
        self.__model = n

    def get_model(self,m):
        return self.__model
