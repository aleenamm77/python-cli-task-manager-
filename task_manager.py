from storage import load_tasks, save_tasks


class TaskManager:

    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        save_tasks(self.tasks)
        print("Task added successfully!")
    
    def list_tasks(self):

        if not self.tasks:
            print("No tasks found.")
            return

        print("\n========== TASKS ==========")

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

        print("===========================\n")