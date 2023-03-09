# Assignment 2 Part 2
# Group 14

# Product Information
PRICE_LIBRARY = {
    "1": ["Apple iPhone", 120.45],
    "2": ["Android Phone", 99.50],
    "3": ["Apple Tablet", 75.69],
    "4": ["Android Tablet", 65.73],
    "5": ["Windows Tablet", 51.49],
}
WEEK_DIVIDE = {
    "2": ["Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]],
    "3": ["Work Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]],
    "4": ["Weekend", ["Saturday", "Sunday"]]
}

print("Welcome to Circle Phones Profit calculator")

while True:

    total_price = 0
    final_price = 0
    days_of_week = 0
    time_period = 0

    print("You can calculate the profit of the company according to a specific day or by a week or divide "
          "the week into weekdays and weekends")
    print("Enter:")
    print("1 - For specific Day")
    print("2 - For the Week")
    print("3 - For Week Business Days")
    print("4 - For Weekend Days")
    print("0 - Exit")

    day_selector_str = input("")
    day_selector_int = int(day_selector_str)

    if day_selector_int == 1:
        days_of_week = [input("Enter a specific Day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")]
        time_period = days_of_week[0]

    elif day_selector_int in range(2, 5):
        days_of_week = WEEK_DIVIDE.get(day_selector_str)[1]
        time_period = WEEK_DIVIDE.get(day_selector_str)[0]

    elif day_selector_int == 0:
        print("Program End!")
        break

    else:
        print("Invalid input, please enter a valid input")
        continue

    for day in days_of_week:

        print(f"For {day}")

        while True:

            category_number_str = input("Enter product number 1-5, or enter 0 to stop:")
            category_number_int = int(category_number_str)

            if category_number_int in range(1, 6):
                quantity_sold = int(input("Enter quantity sold: "))
                price = PRICE_LIBRARY.get(category_number_str)[1]
                product_price = float(price) * quantity_sold
                total_price += product_price

            elif category_number_int == 0:
                final_price = round(total_price, 2)
                break

            else:
                print("Invalid input, please enter a valid number")
                continue

    print(f"Your total profit for the {time_period} is {final_price}")

    if final_price >= 10000:
        print(f"You did well this {time_period}! Keep up the great work!")

    else:
        print(f"We didn’t reach our goal for this {time_period}. More work is needed.")
        
















