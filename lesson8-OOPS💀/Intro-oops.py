#starting Object oriented programming 

#what is class
#---> A class is a blueprint for creating an object


class Car:
    color = "white" 
    brand = "Audi"
    model = "R8"

class Car2:
    color = "green"
    brand = "BMW"
    model = "M5 Competation"

#Creating Objects(Instances)

print("-----Car 1 Information-----")

car1 = Car()
print(car1.brand)
print(car1.model)
print(car1.color)

print("-----Car 2 Information-----")

car2 = Car2()
print(car2.brand)
print(car2.model)
print(car2.color)
