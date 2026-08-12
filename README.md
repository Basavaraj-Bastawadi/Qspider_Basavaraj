# Vehicle Rental System

A simple **Vehicle Rental System** developed using Python and Object-Oriented Programming (OOP) concepts.

## Project Description

This project represents a basic vehicle rental system for different types of vehicles such as **Cars** and **Bikes**.

Each vehicle has common information like:

* Vehicle number
* Brand
* Rental price per day

Different vehicles can also have their own additional information:

* **Car** → Number of seats
* **Bike** → Engine capacity

The program displays vehicle details and calculates the total rental amount based on the number of rental days.

## Project Structure

```text
VehicleRental/
│
├── vehicle.py
├── car.py
├── bike.py
├── main.py
└── README.md
```

## Files Description

### `vehicle.py`

Contains the abstract `Vehicle` class.

It contains the common properties and abstract methods that are shared by all vehicles.

### `car.py`

Contains the `Car` class, which inherits from the `Vehicle` class.

Additional property:

* Number of seats

### `bike.py`

Contains the `Bike` class, which inherits from the `Vehicle` class.

Additional property:

* Engine capacity

### `main.py`

Contains the main program.

It creates Car and Bike objects, stores them in a list, displays their details, and calculates the rental amount.

## OOP Concepts Used

### 1. Abstraction

The `Vehicle` class is an abstract class using Python's `ABC` and `abstractmethod`.

### 2. Inheritance

`Car` and `Bike` inherit common properties and methods from the `Vehicle` class.

### 3. Encapsulation

Vehicle information is stored inside the respective objects.

### 4. Polymorphism

The same methods such as `display_details()` and `calculate_rent()` are used with different types of vehicle objects.

## Rental Calculation

The rental amount is calculated using:

```text
Total Rent = Rental Price Per Day × Number of Days
```

For example:

```text
Rental price = ₹1500 per day
Rental days  = 3

Total rent = ₹1500 × 3
           = ₹4500
```

## How to Run

Make sure Python is installed on your system.

Open the project folder in the terminal and run:

```bash
python main.py
```

## Sample Vehicles

```text
Car:
Number: KA01AB1234
Brand: Toyota
Price: ₹1500/day
Seats: 5

Bike:
Number: KA02CD5678
Brand: Honda
Price: ₹500/day
Engine Capacity: 125 cc
```

## Conclusion

This project demonstrates a simple vehicle rental system using Python OOP concepts. It is designed to be easy to understand and can be extended in the future with additional vehicle types and rental features.
