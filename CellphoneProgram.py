import CellphoneClass as c
import random

def main():
    #Create to Instances for the class Iphone and Andriod
    phone = c.CellPhone('Apple',"Iphone 15",1099) 
   
    #Now we set these up
    phone.set_manufact('Apple')
    phone.set_model('Iphone 15')
    phone.set_price(1099)

    #Display the information nicely
    print(f"Manufacturer is: {phone.get_manufact()}")
    print(f"Model is: {phone.get_model()}")
    print(f"Retail Price: ${phone.get_price()}")


main()