# ==============================================================================
# Python Fundamentals
# Topic       : Recursion
# By          : Pranay Savdekar
# Date        : 09/08/2026
# ==============================================================================


# ==============================================================================
# Problem 1: Factorial of a number using recursion
# ==============================================================================
def fact(n):
    if n==0:             
        return 1
    return n*fact(n-1)
print(fact(5))

# ==============================================================================
# Problem 2: Fibonacci series
# ==============================================================================
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


# ==============================================================================
# Problem 3: Sum of digits using recursion.
# ==============================================================================
def sum_digits(num):
    if num==0:
        return 0
    return num%10 +sum_digits(num//10)
print(sum_digits(493))


# ==============================================================================
# Problem 4: Power of a number — x^n without using **
# ==============================================================================
def power(x,n):
    if n==0:
        return 1
    return x * power(x,n-1)
print(power(3,3))