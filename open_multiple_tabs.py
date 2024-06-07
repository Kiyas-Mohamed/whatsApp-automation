import webbrowser
import time

URLs = ["https://www.python.org", "https://www.google.com", "https://www.example.com"]

for _ in range(9):

    for url in URLs:
        webbrowser.open_new_tab(url)

    time.sleep(0.3)
