import InsectClass as i

def main():
    mosquito = i.Insect() 
    housefly = i.Insect()
    
    #instance needs to call the method
    mosquito.calcflight()
    housefly.calcflight()

    #print the range
    print(f"the mosquito can fly up to {mosquito.get_miles()}")
    print(f"the housefly can fly up to {housefly.get_miles()}")

main()