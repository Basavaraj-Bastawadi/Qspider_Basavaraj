from car import Car
from bike import Bike

def main():
    car = Car("KA01AB1234", "Toyota", 1500, 5)
    bike = Bike("KA02CD5678", "Honda", 500, 125)

    vehicles = [car, bike]

    days = 3

    for vehicle in vehicles:
        vehicle.display_details()

        rent = vehicle.calculate_rent(days)

        print("Rental days:", days)
        print("Total rent:", rent)
        print("--------------------")
main()