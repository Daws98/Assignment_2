# Daily, Weekly and Weekend Profit Calculator
# Author: Dawson Gall

# Dictionary & Variables
phone_price = {
    "1": ["Apple iPhone", 120.45],
    "2": ["Android Phone", 99.50],
    "3": ["Apple Tablet", 75.69],
    "4": ["Android Tablet", 65.73],
    "5": ["Windows Tablet", 51.49],
}
week_period = {
    "1": ["Specific day", ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]],
    "2": ["Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]],
    "3": ["Work Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]],
    "4": ["Weekend", ["Saturday", "Sunday"]],
}

# Print Startup
print("Welcome to Circle Phones' Profit calculator.")

# User Inputs
while True:
    total = 0
    final = 0
    time_period = None
    week_day = None
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
        day_input_int = int(day_input)
    elif day_input == "0":
        print("Program End!")
        break
    else:
        print("Invalid input, please enter a valid")
        continue
    if day_input_int in range(2, 5):
        week_day = week_period.get(day_input)[1]
        time_period = week_period.get(day_input)[0]
    else:
        while True:
            print("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
            date = input("").strip()
            week_input = date.lower()
            if week_input in week_period.get("1")[1]:
                week_day = [week_input.capitalize()]
                time_period = week_day[0]
                break
            else:
                print("Invalid input, please enter a valid input")
                continue
    for day in week_day:
        print(f"For {day}")
        while True:
            print("Enter product number 1-5, or enter 0 to stop:")
            category_input = (input("").strip())
            if category_input in phone_price:
                while True:
                    print("Enter quantity sold:")
                    quantity_sold = input("")
                    if quantity_sold.isdigit():
                        price = phone_price.get(category_input)[1]
                        product_price = float(price) * int(quantity_sold)
                        total += product_price
                        break
                    else:
                        print("Invalid quantity , please enter a valid quantity")
                        continue
            elif category_input == "0":
                final = round(total, 2)
                break
            else:
                print("Invalid product number, please enter a valid product number")
                continue
    print(f"Total profit of {time_period} is ${final}")
    if final >= 10000:
        print(f"You did well this {time_period}! Keep up the great work!")
    else:
        print(f"We didn't reach our goal for this {time_period}. More work is needed.")
