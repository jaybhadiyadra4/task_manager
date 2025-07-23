import json
import os
from models import Task
from utils import export_completed_task_to_csv

class TaskManager:
    def __init__(self, filename='data/tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r') as file:
            data = json.load(file)
            return [Task.from_dict(task) for task in data]

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
        self.save_tasks()

    def mark_task_done(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_completed()
                export_completed_task_to_csv(task)
        self.save_tasks()

    def list_tasks(self, filter_option=None):
        if not self.tasks:
            print("\n🟡 No tasks available yet. Use option [1] to add a new task.")
            return []

        filtered = self.tasks
        if filter_option == "today":
            from datetime import date
            today = date.today().isoformat()
            filtered = [task for task in self.tasks if task.due_date == today]
        elif filter_option == "completed":
            filtered = [task for task in self.tasks if task.completed]
        elif filter_option == "pending":
            filtered = [task for task in self.tasks if not task.completed]

        if not filtered:
            print(f"\n🟡 No tasks found for filter: {filter_option}")
            return []

        return filtered

