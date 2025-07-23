from manager import TaskManager
from models import Task


try:
    def display_menu():
        print("\n📌 Personal Task Manager")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. View Today's Tasks")
        print("6. View Completed Tasks")
        print("7. Exit")

    def main():
        manager = TaskManager()

        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Title: ")
                description = input("Description: ")
                due_date = input("Due Date (YYYY-MM-DD): ")
                priority = input("Priority (Low/Medium/High): ")
                task = Task(title, description, due_date, priority)
                manager.add_task(task)
                print("✅ Task added.")
            elif choice == '2':
                tasks = manager.list_tasks()
                print("\nAll Tasks:")
                for task in tasks:
                    status = "✔️" if task.completed else "❌"
                    print(f"{task.title} | Due: {task.due_date} | {task.priority} | {status}")
            elif choice == '3':
                title = input("Enter title of task to mark done: ")
                manager.mark_task_done(title)
                print("✅ Task marked as completed.")
            elif choice == '4':
                title = input("Enter title of task to delete: ")
                manager.delete_task(title)
                print("🗑️ Task deleted.")
            elif choice == '5':
                tasks = manager.list_tasks(filter_option="today")
                print("\nToday's Tasks:")
                for task in tasks:
                    print(f"{task.title} | Due: {task.due_date} | {task.priority}")
            elif choice == '6':
                tasks = manager.list_tasks(filter_option="completed")
                print("\nCompleted Tasks:")
                for task in tasks:
                    print(f"{task.title} | ✅ Done")
            elif choice == '7':
                print("👋 Exiting Task Manager. Bye!")
                break
            else:
                print("\n❌ Invalid option. Please choose a number between 1 and 7.")

    if __name__ == "__main__":
        main()


except Exception as e:
    print(f"\n⚠️ An unexpected error occurred: {e}")