# Daily, Weekly and Weekend Profit Calculator
# Author: Dawson Gall

# Dictionary & Variables
phone_price = {
    "0": 0,
    "1": 120.45,
    "2": 99.50,
    "3": 75.69,
    "4": 65.73,
    "5": 51.49
}
week_period = {
    "1": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "2": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "3": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "4": ["Saturday", "Sunday"],
}
category = list(phone_price.values())
user_input = 6
total = 0
time_period = None

# Print Startup
print("Welcome to Circle Phones' Profit calculator. You can calculate your profits for a specific day, by week or you "
      "can divide the week into weekdays and the weekend.")

# User Inputs
while True:
    total = 0
    time_period = None
    days = None

    print("Welcome to Circle Phones Profit Calculator")
    print("You can calculate the profit of the company according to a specific day or by a week or divide week into "
          "weekdays and weekend")
    print("Enter:")
    print("1 - For specific day")
    print("2 - For the Week")
    print("3 For Week Business Days")
    print("4 - For Weekend Days")
    print("0 - Exit")
    day_input = input("")
    if day_input in week_period:
        day_selection = int(day_input)
    elif day_input == 0:
        print("Program End!")
        break
    else:
        print("Invalid input, please enter a valid")
        continue
    if day_selection in range(2, 5):
        week_day = week_period[1]
        time_period = week_period[0]
    else:
        while True:
            print("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
            day_name = input("")
            week_day = [day_name]
            time_period = week_day
            if week_day in week_period.get("1")[1]:
                time_period = week_day[0]
                break
            else:
                print("Invalid quantity, please enter a valid quantity")
            continue
    for day in week_day:
        print(f' For {day}')
        while user_input != 0:
            print("Enter product number 1-5, or enter 0 to stop:")
            user_input = int(input(""))
            if user_input > 5 or user_input < 0:
                print('Invalid input, please enter a valid number')
            elif user_input == 0:
                user_input = 6
                break
        else:
            print("Enter quantity sold:")
            amount_sold = int(input(""))
            total += round((category[user_input] * amount_sold), 2)

    print(f"Total profit of {time_period} is ${total}")
    if total <= 10000:
        print(f"You did well this {time_period}! Keep up the great work!")
    else:
        print(f"We didn't reach our goal for this {time_period}. More work is needed.")
