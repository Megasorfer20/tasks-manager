import json
import os

from read_json import get_all_data

print(os.getcwd())

def create_task(new_task,file_path='./database/task.json'):
    try:
        required_fields = {"tittle", "description"}
        
        if not required_fields.issubset(new_task.keys()):
            raise ValueError(f"Missing required fields: {required_fields - new_task.keys()}")
        
        tasks = get_all_data(file_path)
        
        new_task_id = tasks[-1]['task_id'] + 1 if tasks else 1
        
        task_to_add = {
            "task_id": new_task_id,
            "tittle": new_task['tittle'],
            "description": new_task['description'],
            "checked": False
        }
        tasks.append(task_to_add)

        with open(file_path, 'w', encoding='utf-8') as task_document:
            json.dump(tasks, task_document, indent=4, ensure_ascii=False)

        print(f"A new task has been added with ID {new_task_id}.")
        return tasks[len(tasks) - 1]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except ValueError as ve:
        print(f"Validation Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    new_task = {"tittle": "Debug Example", "description": "Descripción prueba"}
    result = create_task(new_task)
    if result:
        print("Task created successfully:", result)
    else:
        print("Failed to create the task.")