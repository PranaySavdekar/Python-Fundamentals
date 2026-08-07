# ==============================================================================
# Python Fundamentals
# Topic       : For Loops
# By          : Pranay Savdekar
# Date        : 07/08/2026
# ==============================================================================


# ==============================================================================
# Problem 1: Print Fibonacci series up to n terms
# ==============================================================================

n=int(input("Enter the number of terms : "))
a=0
b=1
for i in range (n):
    print(a)
    c=a+b
    a=b
    b=c

# ==============================================================================
# Problem 2: Find factorial of a number
# ==============================================================================

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial =", factorial)


# ==============================================================================
# Problem 3: Find sum of numbers from 1 to 100
# ==============================================================================

total_sum = 0
for i in range(1, 101):
    total_sum += i
print("Sum =", total_sum)

# ==============================================================================
# Problem 4: Print multiplication table of a given number
# ==============================================================================

table=int(input("Enter the number for table :"))
for i in range(1,11):
    print(f"{table} x {i} = {table * i}")

# ==============================================================================
# Problem 5: Check if a number is prime
# ==============================================================================

n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

# ==============================================================================
# Problem 6: Find all perfect numbers between 1 and 500
# ==============================================================================
for num in range(1, 501):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num:
        print(num, end=" ")

# ==============================================================================
