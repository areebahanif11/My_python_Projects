'''
features of my project:
Add task, View all task, Mark task as complete, Delete task, Save task to a file, Load task from a file

'''
# function for each feature
def add_task(tasks):
    task = input("Enter the task: ")
    tasks[task] = "incomplete"
    print(f"Task {task} added.")

def view_task(tasks):
    for task, status in tasks.items():
        print(f"{task}: {status}")

def mark_complete(tasks):
    task = input("Enter a task to mark as complete: ").lower()
    if task in tasks:
        tasks[task] = "complete"
        print(f"Task {task} marked as complete.")
    else:
        print(f"Task {task} not found.")

def delete_task(tasks):
    task = input("Enter the task to delete: ").lower()
    if task in tasks:
        # del tasks[task]
        tasks.pop(task)
        print(f"Task {task} deleted.")
    else:
        print(f"Task {task} not found.")

def save_task_to_file(tasks, filename):
    with open(filename,"w") as file:
        for task, status in tasks.items():
            file.write(f"{task},{status}\n")
        print(f"Tasks saved to {filename}.")


def load_tasks_from_file(filename):
    tasks = {}
    with open(filename) as file:
        for line in file:
            task, status = line.lower().strip().split(",")  
            tasks[task] = status
    return tasks

# Main 
filename = "To_Do_file.txt"
tasks = load_tasks_from_file(filename)

while True:
    print("\nTo-Do list Menu: ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as complete")
    print("4. Delete Task")
    print("5. Save Task")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        view_task(tasks)
    elif choice == 3:
        mark_complete(tasks)
    elif choice == 4:
        delete_task(tasks)
    elif choice == 5:
        save_task_to_file(tasks,filename)
        break
    else:
        print("Invalid choice. Please enter from 1-5.")
