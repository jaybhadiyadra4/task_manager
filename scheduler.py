import schedule
import time
from datetime import datetime
from utils import load_tasks

def daily_summary():
    print("\n🔔 Daily Task Summary (" + datetime.now().strftime("%Y-%m-%d") + "):")
    tasks = load_tasks()
    for task in tasks:
        if not task["completed"]:
            print(f"- {task['title']} (Due: {task['due_date']}) [Priority: {task['priority']}]")

def start_scheduler():
    schedule.every().day.at("08:00").do(daily_summary)

    print("📅 Daily summary will print every day at 08:00.")
    while True:
        schedule.run_pending()
        time.sleep(1)


daily_summary()