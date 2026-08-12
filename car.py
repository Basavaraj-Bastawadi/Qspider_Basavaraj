from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, number, brand, price, seats):
        super().__init__(number, brand, price)
        self.seats = seats

    def display_details(self):
        print("Car")
        print("Number:", self.number)
        print("Brand:", self.brand)
        print("Seats:", self.seats)
        print("Price per day:", self.price)

    def calculate_rent(self, days):
        return self.price * days