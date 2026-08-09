# ===========================================================================================================================
# Python Fundamentals
# Topic       : Modules
# By          : Pranay Savdekar
# Date        : 09/08/2026
# ===========================================================================================================================


# ===========================================================================================================================
# Problem 1: Math Module
# Use math module to find sqrt, power, floor, ceil of a number
# ===========================================================================================================================
import math as m 
num = float(input("Enter a number: "))

print(f"Number: {num}")

print(f"Square Root: {m.sqrt(num)}")
print(f"Power of 2: {m.pow(num, 2)}")
print(f"Floor: {m.floor(num)}")
print(f"Ceil: {m.ceil(num)}")
print(f"Factorial: {m.factorial(int(num))}")


# ===========================================================================================================================
# Problem 2: Random Module
# Build a number guessing game - computer picks random number between 1-100
# ===========================================================================================================================

import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1-100: "))
    attempts += 1
    
    if guess < secret:
        print("Too low! Try higher.")
    elif guess > secret:
        print("Too high! Try lower.")
    else:
        print(f"Correct! You got it in {attempts} attempts!")
        break


# ===========================================================================================================================
# Problem 3: DateTime Module
# Print current date, time, day of week
# ===========================================================================================================================

from datetime import datetime

now = datetime.now()

print("Date:", now.date())
print("Time:", now.time())
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Day of Week:", now.strftime("%A"))
print("Month Name:", now.strftime("%B"))

# ===========================================================================================================================
