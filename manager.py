import item

class Manager(object):

    def list(self):
        file = open("todos.txt", "r")

        lines = file.readlines()

        for line in lines:
            section = line.split("|")
            print(f"Task: {section[0]}")
            print(f"When it was made: {section[1]}")
            if section[2] == "True\n":
                print("Is it done?: Completed")
            else:
                print("Is it done?: Not Completed")

    def add(self, item):
        file = open("todos.txt", "a")
        file.write(f"{item.task} | {item.time} | {item.is_task_complete}\n")
        file.close()

    def complete(self,thing):
        file = open("todos.txt", "r+")

        lines = file.readlines()

        index = 0
        for line in lines:
            if job in line:
                section = line.split("|")
                if section[2] == "False\n":
                    section[2] = 'True\n'
                    lines[index] = f"{section[0]},{section[1]},{section[2]}"
                    break

            index += 1
        else:
            print("Sorry, that task was not found.")

        file.truncate(0)

        for line in lines:
            file.write(line)

        file.close()
