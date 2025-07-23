import json
import matplotlib.pyplot as plt
from collections import Counter
from utils import load_tasks


def visualize_completion():
    tasks = load_tasks()
    if not tasks:
        print("\n📉 No tasks to visualize. Add some tasks first.")
        return

    completed = sum(task['completed'] for task in tasks)
    pending = len(tasks) - completed

    plt.pie(
        [completed, pending],
        labels=["Completed", "Pending"],
        autopct='%1.1f%%',
        colors=["green", "orange"]
    )
    plt.title("Task Completion Summary")
    plt.show()


def visualize_priority_distribution():
    tasks = load_tasks()
    if not tasks:
        print("\n📉 No tasks to visualize. Add some tasks first.")
        return

    priorities = [task["priority"] for task in tasks]
    counter = Counter(priorities)

    plt.bar(counter.keys(), counter.values(), color="skyblue")
    plt.title("Tasks by Priority")
    plt.xlabel("Priority")
    plt.ylabel("Number of Tasks")
    plt.show()


visualize_completion()
visualize_priority_distribution()