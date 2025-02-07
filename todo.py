def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            task_number = 1
            for task in file:
                print(f"{task_number}. {task.strip()}")  # Print each task with a task number
                task_number += 1
    except FileNotFoundError:
        print("No tasks available. The file 'tasks.txt' does not exist.")


def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")  # Properly concatenate the task and newline

def delete_task(task_number):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    # Check if the task number is valid
    if 0 < task_number <= len(tasks):
        with open("tasks.txt", "w") as file:
            for i, task in enumerate(tasks):
                if i != task_number - 1:  # Skip the task to be deleted
                    file.write(task)
        print(f"Task {task_number} deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        view_tasks()

    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)

    elif choice == '3':
        view_tasks()
        try:
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        except ValueError:
            print("Please enter a valid task number.")
    else:
        print("Invalid choice")

if __name__=="__main__":
    main()
