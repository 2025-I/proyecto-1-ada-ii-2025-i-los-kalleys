import tkinter as tk
from file_chooser.file_chooser import FileReaderApp

if __name__ == "__main__":
    root = tk.Tk()
    app = FileReaderApp(root)
    root.mainloop()
