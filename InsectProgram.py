import InsectClass as i

def main():
    mosquito = i.Insect(2,4,'Mosquito') 
    housefly = i.Insect(2,4,'Housefly')
    
    #instance needs to call the method
    mosquito.calcflight()
    housefly.calcflight()

    #print the range
    print(f"the {mosquito.get_name()} can fly up to {mosquito.get_miles()}")
    print(f"the {housefly.get_name()} can fly up to {housefly.get_miles()}")

main()