class TodoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f"Task '{task}' removed from the list.")
                return
        print(f"Task '{task}' not found.")

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print(f"Task '{task}' marked as completed.")
                return
        print(f"Task '{task}' not found.")

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for idx, t in enumerate(self.tasks, 1):
                status = "Completed" if t["completed"] else "Not Completed"
                print(f"{idx}. {t['task']} - {status}")

def todo_list_app():
    todo = TodoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            todo.add_task(task)
        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            todo.remove_task(task)
        elif choice == '3':
            task = input("Enter the task you want to mark as completed: ")
            todo.complete_task(task)
        elif choice == '4':
            todo.display_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

todo_list_app()