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

        # Add game title
        self.title_label = tk.Label(
            self.main_menu,
            text="JEOPARDY",
            font=("Arial", 48, "bold"),
            fg="blue"
        )
        self.title_label.pack(pady=50)

        # Add start button
        self.start_button = tk.Button(
            self.main_menu,
            text="Start Game",
            font=("Arial", 20),
            command=self.show_game_modes,
            width=15,
            height=2
        )
        self.start_button.pack(pady=30)

    def show_game_modes(self):
        # Hide main menu
        self.main_menu.pack_forget()

        # Create game modes frame
        self.mode_frame = tk.Frame(self.root)
        self.mode_frame.pack(expand=True, fill='both')

        # Add mode selection title
        mode_label = tk.Label(
            self.mode_frame,
            text="Select Game Mode",
            font=("Arial", 36, "bold")
        )
        mode_label.pack(pady=30)

        # Add mode buttons
        modes = ["Presidents", "Sports", "Music"]
        for mode in modes:
            button = tk.Button(
                self.mode_frame,
                text=mode,
                font=("Arial", 18),
                width=15,
                height=2,
                command=lambda m=mode: self.start_game(m)
            )
            button.pack(pady=10)

    def start_game(self, mode):
        # This will be implemented next
        print(f"Starting game in {mode} mode")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = JeopardyGame(root)
    root.mainloop()
