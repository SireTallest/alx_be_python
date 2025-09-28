
shopping_list = []

def add_item(item):
    """This function adds an item to the shopping list"""
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(item):
    """Function to remove an item from the shopping list"""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not found in the shopping list.")

def show_list():
    """function to display the current items in the shopping list"""
    if shopping_list:
        print("Current Shopping List: ")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

def display_menu():
    print("\n===== Shopping List Manager =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(input("Enter the item to add: "))
        elif choice == '2':
            remove_item(input("Enter the item to remove: "))
        elif choice == '3':
            show_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
