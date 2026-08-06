# ==============================================================================
# Python Fundamentals
# Topic       : While Loops
# Author      : Pranay Savdekar
# Date        : 06/08/2026
# ==============================================================================

# Problem 1: Print numbers from 1 to 100 and count them.
# ==============================================================================

i=1
count=0
while i<=100:
    print(i)
    count+=1
    i+=1
print("total numbers =" ,count)


# ==============================================================================
# Problem 2: Find the sum of digits of a given number (e.g., 1234 → 1+2+3+4 = 10)
# ==============================================================================

num=int(input("Enter the number : "))
sum=0
while num>0:
    digit= num%10
    sum+=digit
    num=num//10
print("The sum of the digits of the given number =",sum)


# ==============================================================================
# Problem 3: Reverse a given number using a while loop.
# ==============================================================================

num=int(input("Enter a number to be reversed : "))
reverse=0
while num>0:
    digit=num%10
    reverse= reverse*10 + digit
    num=num//10
print("Reversed number :",reverse)


# ==============================================================================
# Problem 4: Check if a number is a palindrome using a while loop.
# ==============================================================================

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

# ==============================================================================
# Problem 5: Find and print numbers from 1 to 100 that are divisible by 3 but not by 9
# ==============================================================================

i = 1
while i <= 100:
    if i % 3 == 0 and i % 9 != 0:
        print(i)
    i += 1

# ==============================================================================
# Problem 6: Find largest digit in a number — comparison inside loop
# ==============================================================================

number=int(input("Enter the number : "))
largest =0 
while number>0:
    digit = number%10
    if digit>largest:
        largest= digit
    number=number//10
print("largest number : ", largest)


# ==============================================================================
# Problem 7: Check if a number is a prime number using a while loop.
# ==============================================================================

num = int(input("Enter a number: "))
i = 1
count = 0

while i <= num:
    if num % i == 0:
        count += 1
    i += 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

# ==============================================================================
# Problem 8: Check if a number is an Armstrong number using a while loop.
# ==============================================================================


num = int(input("Enter a number: "))

num_str = str(num)
length = len(num_str)
original_num = num
sum = 0

while num > 0:
  digit = num % 10
  sum = sum + digit ** length
  num //= 10

if sum == original_num:
  print(original_num,"is a armstrong number")
else:
  print(original_num,"is not a armstrong number")


# ==============================================================================

