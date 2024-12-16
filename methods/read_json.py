import json
import os

print(os.getcwd())

def get_all_data(file_path='./database/task.json'):
    try:
        with open(file_path,'r',encoding='utf-8') as tasks:
            return json.load(tasks)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def filter_tasks(condition):
    try:
        tasks = get_all_data()
        return [task for task in tasks if condition(task)]
    except Exception as e:
        print(f"Error filtering tasks: {e}")
        return []

def get_checked_data():
    return filter_tasks(lambda task: task.get('checked') is True)

def get_unchecked_data():
    return filter_tasks(lambda task: task.get('checked') is False)

if __name__ == "__main__":
    print("All data:", get_all_data())
    print("Checked Data:", get_checked_data())
    print("Unchecked Data:", get_unchecked_data())