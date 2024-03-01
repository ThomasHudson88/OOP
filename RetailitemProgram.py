#import the class
import RetailitemClass as r

#initialize the item instances
item1 = r.Retailitem('Jacket',12,59.95)

item2 = r.Retailitem('Designer Jeans',40,34.95)

item3 = r.Retailitem('Shirt',20,24.95)

print(f"Item Description: {item1.get_description()}   Units in Inventory: {item1.get_unitsinventory()}     Price: ${item1.get_price()}")
print(f"Item Description: {item2.get_description()}   Units in Inventory: {item2.get_unitsinventory()}     Price: ${item2.get_price()}")
print(f"Item Description: {item3.get_description()}   Units in Inventory: {item3.get_unitsinventory()}     Price: ${item3.get_price()}")
    