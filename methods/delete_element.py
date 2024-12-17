from sqlalchemy.orm import Session
from database.creation_database import SessionLocal
from models.tasks_model import Task

def delete_task(task_id):
    try:
        session: Session = SessionLocal()

        # Buscar la tarea por ID
        task_to_delete = session.query(Task).filter(Task.id_task == task_id).first()

        if not task_to_delete:
            print(f"No task found with ID {task_id}.")
            session.close()
            return False

        # Eliminar la tarea
        session.delete(task_to_delete)
        session.commit()
        print(f"Task with ID {task_id} has been deleted.")
        session.close()
        return True
    except Exception as e:
        print(f"Error deleting task: {e}")
        return False

if __name__ == "__main__":
    delete_task(1) 
