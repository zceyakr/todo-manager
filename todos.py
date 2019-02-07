import item
import manager


run = manager.Manager()
action = input("""What do you want to do? Do you want to list, add, or complete?
> """)

if action == "list":
    run.list()

elif action == "add":
    print("What task are you adding?")
    new_task = input("> ")
    add_task = item.Items(new_task)
    run.add(add_task)
    print(f"You added the task: {new_task}")

elif action == "complete":
    print("What is the name of the task you'd like to mark as completed?")
    task_to_complete = input("> ")
    run.complete(task_to_complete)

elif action == "quit":
    print("Goodbye.")
    quit()

else:
    print("""Did you mean:
    list - lists the current tasks in the file
    add - let’s you add an additional task to your file
    complete - Let’s you mark a task as complete if it is not completed
    """)
