from sqlalchemy.orm import Session
from database.creation_database import SessionLocal
from models.tasks_model import Task

def toggle_task_checked(task_id):
    try:
        session: Session = SessionLocal()

        # Buscar la tarea por ID
        task = session.query(Task).filter(Task.id_task == task_id).first()

        if not task:
            print(f"No task found with ID {task_id}.")
            session.close()
            return None

        # Cambiar el estado de 'checked'
        task.checked = not task.checked
        session.commit()

        print(f"Task ID {task_id} updated: 'checked' is now {task.checked}.")
        session.close()
        return task
    except Exception as e:
        print(f"Error toggling task 'checked' state: {e}")
        return None

if __name__ == "__main__":
    task_id = 1  
    updated_task = toggle_task_checked(task_id)
    if updated_task:
        print(f"Updated Task: ID={updated_task.id_task}, Checked={updated_task.checked}")
    else:
        print("Failed to update the task.")
