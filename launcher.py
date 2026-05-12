import threading
import webbrowser
import time
import os
from dashboard import app

def start_flask():
    app.run(host="127.0.0.1", port=5000, debug=False)

if __name__ == "__main__":
    t = threading.Thread(target=start_flask)
    t.daemon = True
    t.start()

    # Wait for server to start
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:5000")

    # Keep the app alive
    while True:
        time.sleep(1)
