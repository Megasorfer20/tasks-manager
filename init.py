import webview
from .database.creation_database import initialize_database, SessionLocal
from .models.tasks_model import Task

def main():
    webview.create_window('Task Manager', './frontend/index.html')
    webview.start(debug=True)

if __name__ == '__main__':
    initialize_database()
    main()
