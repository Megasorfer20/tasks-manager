import webview
from database.creation_database import initialize_database, SessionLocal
from models.tasks_model import Task
from methods.add_element import create_task
from methods.change_status import toggle_task_checked
from methods.delete_element import delete_task
from methods.fetch_data import get_all_data, get_checked_data, get_unchecked_data


class API:
    def add_task(self, title, description):
        new_task = {"title": title, "description": description}
        task = create_task(new_task)
        if task:
            return {"status": "success", "message": "Task added successfully"}
        else:
            return {"status": "error", "message": "Failed to add task"}

    def get_tasks(self):
        tasks = get_all_data()
        return [{"id": task.id_task, "title": task.title, "description": task.description, "checked": task.checked} for task in tasks]
    
    def get_checked_tasks(self):
        tasks = get_checked_data()
        return [{"id": task.id_task, "title": task.title, "description": task.description, "checked": task.checked} for task in tasks]
    
    def get_unchecked_tasks(self):
        tasks = get_unchecked_data()
        return [{"id": task.id_task, "title": task.title, "description": task.description, "checked": task.checked} for task in tasks]

    def toggle_task(self, task_id):
        toggle_task_checked(task_id)
        return {"status": "success", "message": "Task toggled successfully"}

    def delete_task(self, task_id):
        delete_task(task_id)
        return {"status": "success", "message": "Task deleted successfully"}


def main():
    initialize_database()
    api = API()
    webview.create_window('Task Manager', './frontend/index.html', js_api=api)
    webview.start(debug=True)


if __name__ == '__main__':
    main()