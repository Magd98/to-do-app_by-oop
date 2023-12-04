class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"{self.title} - {self.description} ({status})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.completed = True
                print(f'Task "{task.title}" marked as completed.')
                return
        print(f'Task "{task_title}" not found.')

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do list.")
        else:
            for task in self.tasks:
                print(task)

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            new_task = Task(title, description)
            todo_list.add_task(new_task)
            print(f'Task "{title}" added to the To-Do list.')
        elif choice == '2':
            title = input("Enter the title of the task to mark as completed: ")
            todo_list.mark_task_as_completed(title)
        elif choice == '3':
            print("\nTo-Do List:")
            todo_list.display_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
