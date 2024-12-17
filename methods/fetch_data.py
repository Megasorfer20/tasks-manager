from sqlalchemy.orm import Session
from database.creation_database import SessionLocal
from models.tasks_model import Task

def get_all_data():
    try:
        session: Session = SessionLocal()
        tasks = session.query(Task).all()
        session.close()
        return tasks
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def filter_tasks(condition):
    try:
        tasks = get_all_data()
        return [task for task in tasks if condition(task)]
    except Exception as e:
        print(f"Error filtering tasks: {e}")
        return []

def get_checked_data():
    return filter_tasks(lambda task: task.checked)

def get_unchecked_data():
    return filter_tasks(lambda task: not task.checked)

if __name__ == "__main__":
    print("All data:", get_all_data())
    print("Checked Data:", get_checked_data())
    print("Unchecked Data:", get_unchecked_data())