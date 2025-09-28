import datetime

def display_current_datetime():
 
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)


def calculate_future_date(days_to_add):
   
    current_date = datetime.datetime.now()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future Date after {days_to_add} days:", formatted_future)


def main():
    
    display_current_datetime()

    try:
        days = int(input("Enter number of days to add to current date: "))
        calculate_future_date(days)
    except ValueError:
        print("⚠️ Please enter a valid integer for days.")


if __name__ == "__main__":
    main()
