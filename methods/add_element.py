from sqlalchemy.orm import Session
from database.creation_database import SessionLocal
from models.tasks_model import Task

def create_task(new_task):
    try:
        required_fields = {"title", "description"}
        if not required_fields.issubset(new_task.keys()):
            raise ValueError(f"Missing required fields: {required_fields - new_task.keys()}")

        session: Session = SessionLocal()

        task_to_add = Task(
            title=new_task['title'],
            description=new_task['description'],
            checked=new_task.get('checked', False)
        )
        session.add(task_to_add)
        session.commit()

        print(f"A new task has been added with ID {task_to_add.id_task}.")
        session.close()
        return task_to_add
    except Exception as e:
        print(f"Error creating task: {e}")
        return None

if __name__ == "__main__":
    new_task = {"title": "Debug Example", "description": "Descripción prueba"}
    result = create_task(new_task)
    if result:
        print("Task created successfully:", result)
    else:
        print("Failed to create the task.")
