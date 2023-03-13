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
total = 0
time_period = None
category_number = 6

# User Inputs
print('Welcome to Circle Phones’ Profit calculator.')
print('You can calculate the profit of the company according to a specific day or by a week')
print('or divide the week into weekdays and weekend')
print('Enter:')
print('1 - For specific Day')
print('2 - For the Week')
print('3 - For Week Business Days')
print('4 - For Weekend days')
print('0 - Exit')
while time_period == None:
    day_input = int(input())
    if day_input == 1:
        specific_day = input('Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]')
        days = []
        days.append(specific_day)
        time_period = specific_day
    elif day_input == 2:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        time_period = 'the Week'
    elif day_input == 3:
        time_period = 'the buisness days this week'
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    elif day_input == 4:
        time_period = 'the weekend'
        days = ['Saturday', 'Sunday']
    elif day_input == 0:
        break
    else:
        print("please enter a number between 0 and 4")


for day in days:
    print(f' For {day}')
    while category_number != 0:
        category_number = int(input("Enter product number 1-5, or enter 0 to stop:"))
        if category_number > 5 or category_number < 0:
          print('Invalid input, please enter a valid number')
        elif category_number == 0:
            category_number = 6
            break
        else:
            amount_sold = int(input('Enter quantity sold:'))
            total += round((category[category_number] * amount_sold), 2)

print(f'total profit of {time_period} is ${total}')
if total > 10000:
    print('You did well this period! Keep up the great work!')
else:
    print('We didn’t reach our goal for this period. More work is needed.')
print('Done')
