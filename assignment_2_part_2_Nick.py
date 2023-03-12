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

# Sections of the week and which days are included
WEEK_DIVIDE = {
    "1": ["Specific day ", ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]],
    "2": ["Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]],
    "3": ["Work Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]],
    "4": ["Weekend", ["Saturday", "Sunday"]]
}

print("Welcome to Circle Phones Profit calculator")

while True:

    total_price = 0
    final_price = 0
    days_of_week = None
    time_period = None

    print("You can calculate the profit of the company according to a specific day or by a week or divide "
          "the week into weekdays and weekends")
    print("Enter:")
    print("1 - For specific Day")
    print("2 - For the Week")
    print("3 - For Week Business Days")
    print("4 - For Weekend Days")
    print("0 - Exit")

    day_selector = input("")

    if day_selector in WEEK_DIVIDE:
        day_selector_int = int(day_selector)

    elif day_selector == "0":
        print("Program End!")
        break

    else:
        print("Invalid input, please enter a valid input")
        continue

    if day_selector_int in range(2, 5):
        days_of_week = WEEK_DIVIDE.get(day_selector)[1]
        time_period = WEEK_DIVIDE.get(day_selector)[0]

    else:

        while True:

            print("Enter a specific Day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
            specific_day = input("").strip()
            day_of_week = specific_day.lower()

            if day_of_week in WEEK_DIVIDE.get("1")[1]:
                days_of_week = [day_of_week.capitalize()]
                time_period = days_of_week[0]
                break

            else:
                print("Invalid input, please enter a valid input")
                continue

    for day in days_of_week:

        print(f"For {day}")

        while True:

            print("Enter product number 1-5, or enter 0 to stop:")
            category_number = input("").strip()

            if category_number in PRICE_LIBRARY:

                while True:

                    print("Enter quantity sold: ")
                    quantity_sold = (input(""))

                    if quantity_sold.isdigit():
                        price = PRICE_LIBRARY.get(category_number)[1]
                        product_price = float(price) * int(quantity_sold)
                        total_price += product_price
                        break

                    else:
                        print("Invalid quantity, please enter a valid quantity")
                        continue

            elif category_number == "0":
                final_price = round(total_price, 2)
                break

            else:
                print("Invalid product number, please enter a valid product number")
                continue

    print(f"Your total profit for the {time_period} is ${final_price}")

    if final_price >= 10000:
        print(f"You did well this {time_period}! Keep up the great work!")

    else:
        print(f"We did not reach our goal for this {time_period}. More work is needed.")

        
















