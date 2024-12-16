import webview

def main():
    webview.create_window('Task Manager', './frontend/index.html')
    webview.start(debug=True)

if __name__ == '__main__':
    main()
