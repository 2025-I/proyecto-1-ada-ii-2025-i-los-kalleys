import os
import tkinter as tk
from file_chooser.file_chooser import FileReaderApp


def is_headless():
    return os.environ.get("DISPLAY") is None


if __name__ == "__main__":
    if is_headless():
        print("Running in headless mode. GUI will not be displayed.")
    else:
        root = tk.Tk()
        app = FileReaderApp(root)
        root.mainloop()
