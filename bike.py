from vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, number, brand, price, engine_capacity):
        super().__init__(number, brand, price)
        self.engine_capacity = engine_capacity

    def display_details(self):
        print("Bike")
        print("Number:", self.number)
        print("Brand:", self.brand)
        print("Engine Capacity:", self.engine_capacity, "cc")
        print("Price per day:", self.price)

    def calculate_rent(self, days):
        return self.price * days

    