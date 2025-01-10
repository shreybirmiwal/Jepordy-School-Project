import tkinter as tk
from tkinter import ttk

class JeopardyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeopardy Game")
        self.root.geometry("800x600")

        # Create main menu frame
        self.main_menu = tk.Frame(self.root)
        self.main_menu.pack(expand=True, fill='both')



# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = JeopardyGame(root)
    root.mainloop()
