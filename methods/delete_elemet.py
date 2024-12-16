import json
import os

from read_json import get_all_data

print(os.getcwd())

def delete_task(task_id, file_path='./database/task.json'):
    try:
        tasks = get_all_data(file_path)
        updated_tasks = [task for task in tasks if task.get('task_id') != task_id]

        with open(file_path, 'w', encoding='utf-8') as task_document:
            json.dump(updated_tasks, task_document, indent=4, ensure_ascii=False)

        print(f"Task with ID {task_id} has been deleted.")
        return updated_tasks
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

if __name__ == "__main__":
    print(delete_task(0))