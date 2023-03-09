# Assignment 2 Part 1
# Group 14

# Product Information
PRICE_LIBRARY = {
    "1": ["Apple iPhone", 120.45],
    "2": ["Android Phone", 99.50],
    "3": ["Apple Tablet", 75.69],
    "4": ["Android Tablet", 65.73],
    "5": ["Windows Tablet", 51.49],
}
total_price = 0

# Program Start
print("Welcome to Circle Phones' Profit calculator")

# Price Calculations
while total_price >= 0:

    category_number = int(input("Enter product number 1-5, or enter 0 to stop:"))

    if category_number in range(1, 6):
        quantity_sold = int(input("Enter quantity sold: "))
        product_price = float(PRICE_LIBRARY.get(str(category_number))[1] * quantity_sold)
        total_price += product_price

    elif category_number == 0:
        final_price = round(total_price, 2)
        print(f"Your total profit for today is {final_price}")
        break

    else:
        print("Invalid input, please enter a valid number")
        continue















