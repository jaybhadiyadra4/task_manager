class Task:
    def __init__(self, title, description, due_date, priority, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date  # string format: YYYY-MM-DD
        self.priority = priority  # Low, Medium, High
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        """Convert the task into a dictionary for saving to file."""
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        """Create a Task object from a dictionary (when loading from file)."""
        return Task(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            priority=data["priority"],
            completed=data.get("completed", False)
        )
