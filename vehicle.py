from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price

    @abstractmethod
    def display_details(self):
        pass

    @abstractmethod
    def calculate_rent(self, days):
        pass