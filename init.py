import webview
import sys
import json
import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from database.creation_database import initialize_database
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

    def export_tasks_to_json(self):
        tasks = self.get_tasks()
        filename = "tasks_export.json"
        filepath = os.path.join(os.getcwd(), filename)
        
        current_dir = os.getcwd()
        absolute_path = os.path.join(current_dir, filename)
    
        try:
            print(f"Guardando tareas en: {filepath}")  # Registro de depuración
            with open(filepath, "w", encoding="utf-8") as json_file:
                json.dump(tasks, json_file, indent=4, ensure_ascii=False)
            print("Archivo exportado exitosamente")  # Registro de éxito
            return {"status": "success", "message": f"Tasks exported successfully", "filename": filename, "path": absolute_path }
        except Exception as e:
            print(f"Error al exportar tareas: {str(e)}")  # Registro del error
            return {"status": "error", "message": f"Failed to export tasks: {str(e)}"}

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()


def start_http_server():
    httpd = HTTPServer(('localhost', 8000), CORSRequestHandler)
    print("Serving files with CORS at http://localhost:8000")
    httpd.serve_forever()


def main():
    initialize_database()
    
    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.join(sys._MEIPASS, 'frontend')
    else:
        base_path = './frontend'
    
    print(base_path)
    
    html_path = os.path.join(base_path, 'index.html')
    
    api = API()
    
    threading.Thread(target=start_http_server, daemon=True).start()
    webview.create_window('Task Manager', html_path, js_api=api)
    webview.start()


if __name__ == '__main__':
    main()