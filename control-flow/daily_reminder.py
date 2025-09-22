task = input("Enter your task: ")
priority = input("What is the priority of this task (high/medium/low)?: ").lower()
time_bound = input("Is this task a time-bound task (yes or no)?: ").lower()

match priority:
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a medium priority task. Don't delay it for too long.")
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Do this as soon as possible!")
    case _:
        print("Invalid priority entered.")