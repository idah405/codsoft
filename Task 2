tasks = []

def Track_tasks():
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks added yet.")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully.")

def delete_task():
    Track_tasks()
    if tasks:
        try:
            index = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                print(f"Task '{deleted_task}' Task successfully deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
while True:
    print("\na). Track tasks")
    print("b). Add task")
    print("c). delete task")
    print("d). Exit")
    
    option = input("Please chose from the provided  options only: ")
    
    if option == 'a':
        Track_tasks()
    elif option == 'b':
        add_task()
    elif option == 'c':
        delete_task()
    elif option == 'd':
        print("Exiting...")
        break
    else:
        print("You chose an invalid option. Please chose from the provided  options only.")
