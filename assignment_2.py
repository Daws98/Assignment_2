# Daily Profit Calculator
# Author: Dawson Gall

# Dictionary
phone_price = {
    "0": 0,
    "1": 120.45,
    "2": 99.50,
    "3": 75.69,
    "4": 65.73,
    "5": 51.49
}
category = list(phone_price.values())
user_input = 6
amount_sold = 0
total = 0

# User Inputs
print('Welcome to Circle Phones’ Profit calculator.')
while user_input != 0:
    print("Enter product number 1-5, or enter 0 to stop:")
    user_input = int(input(""))
    if user_input > 5 or user_input < 0:
        print("Invalid input, please enter a valid number")
    elif user_input == 0:
        print(f"Your total profit for today is {total}$")
        break
    else:
        print("Enter quantity sold:")
        amount_sold = int(input(""))
        total += round((category[user_input] * amount_sold), 2)

