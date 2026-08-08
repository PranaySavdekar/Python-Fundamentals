# ================================================================================================================================================
# Python Practice Problems
# By: Pranay Savdekar
# Date: 05/08/2026
# ================================================================================================================================================


# Problem 1: ATM Simulation
# WAP to simulate ATM operations using match-case (1 = Check Balance, 2 = Withdraw, 3 = Deposit, 4 = Exit).
# ================================================================================================================================================
bank_balance=99999
print("Press 1 for Checking Balance")
print("Press 2 for withdraw")
print("Press 3 for deposit")
print("Press 4 for exit")

choice = input("Enter the choice(1-4): ")
match choice:
    case "1":
        print("Your current balance is:", bank_balance)

    case "2":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > bank_balance:
            print("Insufficient balance!")
        else:
            bank_balance = bank_balance - amount
            print("Amount withdrawn successfully")
            print("Remaining balance:", bank_balance)

    case "3":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Enter a valid amount.")
        else:
            bank_balance = bank_balance + amount
            print("Amount deposited successfully")
            print("Updated balance:", bank_balance)

    case "4":
        print("Thank you for using the ATM. Goodbye!")
    case _:
        print("Invalid choice. Please select 1-4.")
# ==============================================================================================================================================================================================================================================

# Problem 2:
# A retail store offers discounts based on the total purchase amount.
#  WAP that takes the purchase amount and applies:
# 20% discount if above 1000
# 10% discount if between 500 and 1000
# No discount if below 500
# ================================================================================================================================================

purchase_amount=int(input("Enter the purchase amount:"))
if purchase_amount>1000:
    discount=purchase_amount*20/100
    print(f"You are eligible for 20% discount. Your discount is {discount} and your total amount is {purchase_amount-discount}")
elif purchase_amount>=500 and purchase_amount<=1000:
    discount=purchase_amount*10/100
    print(f"You are eligible for 10% discount. Your discount is {discount} and your total amount is {purchase_amount-discount}")
else:
    print(f"You are not eligible for any discount. Your purchase amount is {purchase_amount}")
    
# ================================================================================================================================================================================================
# Problem 3: Login System 
# Simulate a basic login system where the user is first asked for their username.
#  If the username is correct, then the program should ask for the password. If both are correct, grant access.
# ================================================================================================================================================
username="admin123"
password="10987"

user_name=str(input("Enter the username: "))
if user_name==username:
    pass_word=(input("Enter the password: "))
    if pass_word==password:
        print("Access Granted")
    else:
         print("Invalid password,Access Denied")
else:
    print("Invalid Username")
# ================================================================================================================================================================================================
