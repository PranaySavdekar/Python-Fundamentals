# ===========================================================================================================================
# Python Fundamentals
# Topic       : Functions
# By          : Pranay Savdekar
# Date        : 08/08/2026
# ===========================================================================================================================


# ===========================================================================================================================
# Problem 1: Sum of digits of a number
# Task: Write a function that accepts an integer and returns the sum of its digits.
#  For example, 1234 should return 10. Make sure it works for negative numbers too (treat -123 same as 123).
# ===========================================================================================================================
def sum_of_digits(num):
    num = abs(num)
    digit_sum = 0
    while num > 0:
        digit = num % 10
        digit_sum += digit
        num //= 10
    return digit_sum


print(sum_of_digits(1534))
print(sum_of_digits(-2453))

# ===========================================================================================================================
# Problem 2: Reverse a number
# Task: Write a function that reverses a given integer. For example, 1234 should return 4321. 
# If the number is negative, keep the sign (-123 → -321).
# ===========================================================================================================================
def reverse_number(num):
    is_negative = num < 0
    num = abs(num)
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return -rev if is_negative else rev

print(reverse_number(4563)) 
print(reverse_number(-635)) 


# ===========================================================================================================================
# Problem 3: Fibonacci series up to n terms
# Task: Write a function that generates the Fibonacci series up to n terms.
#  If n is 0 or negative, return an empty list. 
# For example, if n is 5, output should be [0, 1, 1, 2, 3].
# ===========================================================================================================================
def fibonacci(n):
    if n <= 0:
        return []
    fib = []
    a, b = 0, 1
    for i in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

print(fibonacci(5))    
print(fibonacci(-3))


# ===========================================================================================================================
# Problem 4: Write a function that takes a number and checks if it is a palindrome without using strings.
# ===========================================================================================================================
def palindrome(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return original == rev

print(palindrome(121))
print(palindrome(123))
        

# ===========================================================================================================================
# Problem 5 :Write a function that takes two positive integers and returns their Least Common Multiple (LCM).
# Make sure it works if the numbers are equal.
# ===========================================================================================================================
def find_lcm(num1,num2):
    if num1>num2:
        lcm=num1
    else:
        lcm=num2
    while True:
        if lcm%num1==0 and lcm%num2==0:
            return lcm
        lcm+=1

print(find_lcm(20,25))

# ===========================================================================================================================
#Problem 6: Write a function that takes any number of numbers and returns their sum
# ===========================================================================================================================
def total_sum(*nums):
    total = 0
    for i in nums:
        total += i
    return total

print(total_sum(1, 2, 3))

# ===========================================================================================================================
# Problem7: Write a function that takes any keyword arguments and prints them as a profile
# ===========================================================================================================================
def show_profile(**details):
    for key, value in details.items():
        print(f"{key} : {value}")

show_profile(name="Unknown", age=21, city="Indore")
# ===========================================================================================================================