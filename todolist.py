def display_tasks(tasks):
    print("Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks, task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nOptions: 1-Add, 2-Remove, 3-Show, 4-Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            task = input("Enter new task: ")
            add_task(tasks, task)
        elif choice == "2":
            task_number = int(input("Enter task number to remove: "))
            remove_task(tasks, task_number)
        elif choice == "3":
            display_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
