# ==============================================================================================================================================================
# Python Fundamentals
# Topic       : OOP Basics — Classes, Objects, Attributes, Methods
# By          : Pranay Savdekar
# Date        : 13/08/2026
# ==============================================================================================================================================================


# ==============================================================================================================================================================
# Problem 1: Shopping Cart 
# Create a Cart class with customer name and a list of items.
# Add a method to add an item and another method to display all items in the cart.
# ==============================================================================================================================================================
class Cart:
    def __init__(self,customer_name):
        self.customer_name     =  customer_name
        self.items= []

    def add_item(self,item):
        self.items.append(item)

    def display_items(self):
        print(f"Customer: {self.customer_name}")
        print("Items in cart:")

        for item in self.items:
            print(item)
        

cart = Cart("Drake Parker")

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

cart.display_items()


# =================================================================================================================================================o=============
# Problem 2: # Car Rental Service 
# Design a Car class that stores the car model, number plate, and rent per day.
# Add a method to rent the car (mark it as unavailable) and another method to display car details
# ==============================================================================================================================================================
class Car:
    def __init__(self, model, no_plate, rent_per_day):
        self.model = model
        self.no_plate = no_plate
        self.rent_per_day = rent_per_day
        self.available = True

    def car_on_rent(self):
        self.available = False

    def show_details(self):
        print(f"Model: {self.model}, Number Plate: {self.no_plate}, Rent per day: {self.rent_per_day}, Available: {self.available}")


car1 = Car("BMW", "MP09AB1234", 5000)
car1.show_details()
car1.car_on_rent()
car1.show_details()



# ==============================================================================================================================================================
# Problem 3: # Restaurant Order
#  Design an Order class with order ID, list of items, and total amount.
#  Add a method to add an item to the order and display the final bill. 
# ==============================================================================================================================================================
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.total_amount = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_amount += price

    def show_bill(self):
        print(f"Order ID: {self.order_id}")
        print(f"Items: {self.items}")
        print(f"Total Amount: {self.total_amount}")


order1 = Order(101)

order1.add_item("Burger", 200)
order1.add_item("Pizza", 300)

order1.show_bill()



# ==============================================================================================================================================================
    # Problem 4: Library Member Card 
    # Create a LibraryMember class with name, member ID, and number of books issued. 
    # Add methods to issue a book (increase count) and return a book (decrease count).
# ==============================================================================================================================================================
class LibraryMember:
    def __init__(self, name, memberID, no_of_books_issued):
        self.name = name
        self.memberID = memberID
        self.no_of_books_issued = no_of_books_issued

    def bookissue(self):
        self.no_of_books_issued += 1
        print(f"Book issued to {self.name} Total books = {self.no_of_books_issued}")

    def bookreturn(self):
        self.no_of_books_issued -= 1
        print(f"Book returned by {self.name} Total books = {self.no_of_books_issued}")

m1 = LibraryMember("Drake", 101, 0)
m2 = LibraryMember("Rcky", 102, 8)
m1.bookissue()
m2.bookreturn()




# ==============================================================================================================================================================
# Problem 5: Parking Lot 
# Design a ParkingSpot class with spot number, vehicle number, and availability.
#  Add a method to park a vehicle (mark spot as unavailable) and remove vehicle (make spot available).
# ==============================================================================================================================================================

class ParkingSpot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        self.vehicle_number = None
        self.available = True

    def park_vehicle(self, vehicle_number):
        self.vehicle_number = vehicle_number
        self.available = False

    def remove_vehicle(self):
        self.vehicle_number = None
        self.available = True


spot1 = ParkingSpot(101)

spot1.park_vehicle("MP09AB1234")
print(spot1.vehicle_number, spot1.available)

spot1.remove_vehicle()
print(spot1.vehicle_number, spot1.available)



# ==============================================================================================================================================================
# Problem 6:  Bus Reservation Design a Bus class with bus number, route, total seats, and booked seats. 
# Add a method to book a seat and display available seats.
# ==============================================================================================================================================================

class Bus:
    def __init__(self, bus_number, route, total_seats):
        self.bus_number = bus_number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Seat booked")
        else:
            print("No seats available")

    def show_available_seats(self):
        available = self.total_seats - self.booked_seats
        print(f"Available seats: {available}")


bus1 = Bus(101, "Indore to Bhopal", 40)

bus1.book_seat()
bus1.book_seat()
bus1.show_available_seats()



# ==============================================================================================================================================================
# Problem 7: Water Bottle Create a Bottle class with capacity, brand name, and current water level.
#  Add a method to fill the bottle and another to drink water (reduce level).
# ==============================================================================================================================================================
class Bottle:
    def __init__(self, capacity, brand_name):
        self.capacity = capacity
        self.brand_name = brand_name
        self.water_level = 0

    def fill_bottle(self):
        self.water_level = self.capacity

    def drink_water(self, amount):
        if amount <= self.water_level:
            self.water_level -= amount
        else:
            print("Not enough water")

    def show_level(self):
        print(f"Water level: {self.water_level} ml")


bottle1 = Bottle(1000, "Milton")

bottle1.fill_bottle()
bottle1.show_level()

bottle1.drink_water(300)
bottle1.show_level()






# ==============================================================================================================================================================
# Problem 8: Donation Tracker 
# Create a Donation class with donor name, amount donated, and total donations (class variable). 
# Add methods to make a donation and display donor info.

# Steps:
# Define the Donation class.
# Use a class variable for total donations.
# Constructor sets donor name and amount.
# make_donation method adds amount to total donations.
# show_info method displays donor name, amount, and total donations.
# ==============================================================================================================================================================
class Donation:
    total_donations = 0

    def __init__(self, donor_name, amount):
        self.donor_name = donor_name
        self.amount = amount

    def make_donation(self):
        Donation.total_donations += self.amount

    def show_info(self):
        print(f"Donor: {self.donor_name}")
        print(f"Amount: {self.amount}")
        print(f"Total donations: {Donation.total_donations}")


donation1 = Donation("Drake", 500)
donation1.make_donation()
donation1.show_info()

donation2 = Donation("John", 1000)
donation2.make_donation()
donation2.show_info()


# ==============================================================================================================================================================
# Problem 9: Online Shopping System 
# Create a Product class with product name, price, and stock quantity. 
# Add methods to purchase the product (reduce stock) and restock it. Add a method to display product details with current stock status.

# Steps:
# Define the Product class.
# Create a constructor (__init__) to initialize name, price, and quantity.
# Write a purchase method to reduce stock if enough items are available.
# Write a restock method to increase stock.
# Write a show_info method to display details.
# ==============================================================================================================================================================
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def purchase(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print("Purchase successful")
        else:
            print("Not enough stock")

    def restock(self, amount):
        self.quantity += amount

    def show_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Stock: {self.quantity}")


product1 = Product("Headphones", 2000, 10)

product1.show_info()

product1.purchase(2)
product1.show_info()

product1.restock(5)
product1.show_info()



# ==============================================================================================================================================================
# Problem 10: Online Quiz System 
# Create a Quiz class with quiz name, total questions, and correct answers. 
# Add methods to submit an answer (increment correct count) and calculate percentage score.

# Steps:
# Define the Quiz class.
# Constructor should initialize quiz name, total questions, and correct answers (start with 0).
# Add submit_answer method to update correct answers.
# Add calculate_score method to return percentage score.
# ==============================================================================================================================================================
class Quiz:
    def __init__(self, quiz_name, total_questions):
        self.quiz_name = quiz_name
        self.total_questions = total_questions
        self.correct_answers = 0

    def submit_answer(self, correct):
        if correct:
            self.correct_answers += 1

    def calculate_score(self):
        score = (self.correct_answers / self.total_questions) * 100
        print(f"Score: {score}%")


quiz1 = Quiz("Python Quiz", 5)

quiz1.submit_answer(True)
quiz1.submit_answer(True)
quiz1.submit_answer(False)
quiz1.submit_answer(True)
quiz1.submit_answer(False)

quiz1.calculate_score()




# ==============================================================================================================================================================