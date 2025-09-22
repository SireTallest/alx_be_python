task = input("Enter your task: ").lower()
Priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match Priority:
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