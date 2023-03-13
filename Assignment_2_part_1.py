# Assignment 2
# Group 14

# values
products = {
    'nothing': 0,
    'apple_iphone': 120.45,
    'android_phone': 99.50,
    'apple_tablet': 75.69,
    'android_tablet': 65.73,
    'windows_tablet': 51.49
}
category = list(products.values())
category_number = 6
total = 0

# User Inputs
print('Welcome to Circle Phones’ Profit calculator.')
while category_number != 0:
    category_number = int(input("Enter product number 1-5, or enter 0 to stop:"))
    if category_number > 5 or category_number < 0:
        print('Invalid input, please enter a valid number')
    elif category_number == 0:
        print(f'${total}')
        break
    else:
        amount_sold = int(input('Enter quantity sold:'))
        total += round((category[category_number] * amount_sold), 2)
