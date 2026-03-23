import os
import argparse


TASK_FILE = ("list.txt")


def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """ 
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
    print(f"{task} has been added to your list")
    


def list_tasks():
    """Function: List_task
    
    Input - nothing 
    Return - a list of the tasks
    """
    # 1. Check if the file exists first
    if not os.path.exists(TASK_FILE):
        print("--- Your todo list is currently empty! ---")
        return []

    # 2. If it DOES exist, then open and read it
    with open(TASK_FILE, "r") as file:
        tasks = file.readlines()
    
    # 3. Print them
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task.strip()}")
        
    return tasks


def remove_task(index):
    return

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
