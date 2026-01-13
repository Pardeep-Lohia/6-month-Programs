# Object-Oriented Programming (OOP) in Python
# This file covers key OOP concepts with examples.

# 1. Classes and Objects
# A class is a blueprint for creating objects. An object is an instance of a class.

class Car:
    def __init__(self, make, model, year):
        self.make = make  # Instance variable
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating objects (instances)
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

print("1. Classes and Objects:")
print(car1.display_info())
print(car2.display_info())

# 2. Encapsulation
# Encapsulation hides the internal state of an object and restricts access to it.

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)

print("\n2. Encapsulation:")
print(f"Balance: {account.get_balance()}")

# 3. Inheritance
# Inheritance allows a class to inherit attributes and methods from another class.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} vehicle started."

class ElectricCar(Vehicle):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)  # Call parent constructor
        self.battery_capacity = battery_capacity

    def charge(self):
        return f"{self.brand} is charging. Battery: {self.battery_capacity}kWh"

e_car = ElectricCar("Tesla", 75)

print("\n3. Inheritance:")
print(e_car.start())
print(e_car.charge())

# 4. Polymorphism
# Polymorphism allows methods to do different things based on the object.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print("\n4. Polymorphism:")
print(animal_sound(dog))
print(animal_sound(cat))

# 5. Abstraction
# Abstraction hides complex implementation details and shows only essential features.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(10, 5)

print("\n5. Abstraction:")
print(f"Rectangle area: {rect.area()}")

# 6. Example: Refactoring Procedural Code to OOP
# Original procedural code from user_menu_bill_gst.py can be refactored into classes.

class User:
    def __init__(self, name, address, mobile):
        self.name = name
        self.address = address
        self.mobile = mobile

class Menu:
    def __init__(self):
        self.items = {
            "Pizza": 250,
            "Burger": 30,
            "Pasta": 150,
            "Momos": 100
        }

    def get_price(self, item):
        return self.items.get(item.title(), None)

class Order:
    def __init__(self, user, menu):
        self.user = user
        self.menu = menu
        self.items = []

    def add_item(self, item, quantity):
        price = self.menu.get_price(item)
        if price:
            self.items.append((item, quantity, price))
        else:
            print("Item not found.")

    def calculate_total(self):
        subtotal = sum(qty * price for _, qty, price in self.items)
        gst = subtotal * 0.18
        return subtotal + gst

# Example usage
user = User("John Doe", "123 Main St", "1234567890")
menu = Menu()
order = Order(user, menu)
order.add_item("Pizza", 2)
order.add_item("Burger", 1)

print("\n6. OOP Refactoring Example:")
print(f"Total bill: Rs.{order.calculate_total()}")
