# A simple to do app in Python

data = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Mark Task as done")
    print("3. View Task")
    print("4. Exit")



while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")
    try: 
        if choice == "1":
            task = input("Enter the task you want to add: ")
            data.append(task)
            print("Added item", task)
        elif choice == "2":
            task = input("Enter the task you want to mark as done: ")
            if task in data:
                data.remove(task)
                print("Marked item", task, "as done")
            else:
                print("Task not found")
        elif choice == "3":
            if not data:
                print("No tasks in the list")
            else:
                for tasks in data:
                    print("Your tasks are:", tasks)

        elif choice == "4":
            print("Exiting the to-do list app. Goodbye!")
            break
    except:
        print("An error occurred. Please try again.")
