import csv
import os
import json
from datetime import datetime

# File path where tasks are saved
DATA_FILE = "data/tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def validate_date(date_str):
    """Check if the input string is a valid YYYY-MM-DD date."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def export_completed_task_to_csv(task, filename="data/completed_tasks.csv"):
    """Appends a completed task to CSV."""
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Title", "Description", "Due Date", "Priority"])
        writer.writerow([task.title, task.description, task.due_date, task.priority])