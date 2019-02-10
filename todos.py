from item import Items
from manager import Manager

run = Manager()

while True:
    action = input("""
What do you want to do? Do you want to list, add, complete, or quit?
    > """)

    if action == "list":
        run.list()

    elif action == "add":
        print("\nWhat task are you adding?")
        new_task = input("> ")
        add_task = Items(new_task)
        run.add(add_task)
        print(f"\nYou added the task: {new_task}")

    elif action == "complete":
        print("\nWhat is the name of the task you'd like to mark as completed?")
        task_to_complete = input("> ")
        run.complete(task_to_complete)

    elif action == "quit":
        print("\nGoodbye.\n")
        exit()

    else:
        print("""
Did you mean:
        list - Lists the current tasks in the file.
        add - Let’s you add an additional task to your file.
        complete - Let’s you mark a task as complete if it is not completed.
        quit - Quits out of the todo manager.
        """)
