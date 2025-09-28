from datetime import datetime
from datetime import timedelta

# now = datetime.now()
# print("Current date and time:", now)

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

display_current_datetime()

def calculate_future_date(number_of_days):
    """Calculates the date after a given number of days."""
    future_date = datetime.now() + timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

calculate_future_date(int(input("Enter the number of days to add to the current date: ")))
