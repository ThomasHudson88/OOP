import CarClass as c

#create the attribute instance
car1 = c.Car('2024','Tesla',0)

#Accelrate 5 times, display current speed each time
for i in range(5):
    car1.accelerate()
    print(f"Current Speed: {car1.get_speed()}")

for i in range(5):
    car1.brake()
    print(f"Current Speed: {car1.get_speed()}")