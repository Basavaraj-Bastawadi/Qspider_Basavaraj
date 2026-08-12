from car import Car
from bike import Bike


car = Car("KA01AB1234", "Toyota", 1500, 5)

bike = Bike("KA02CD5678", "Honda", 500, 125)


# Car details
car.display_details()

days = 3
rent = car.calculate_rent(days)

print("Rental days:", days)
print("Total rent:", rent)
print("--------------------")


# Bike details
bike.display_details()

days = 3
rent = bike.calculate_rent(days)

print("Rental days:", days)
print("Total rent:", rent)
print("--------------------")
