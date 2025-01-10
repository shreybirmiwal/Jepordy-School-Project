import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



PRESIDENT_QUESTIONS = {
    "Presidential Facts": [
        {"question": "This president was the first to live in the White House", "answer": "Who is John Adams?", "value": 100},
        {"question": "He was the tallest US president at 6'4\"", "answer": "Who is Abraham Lincoln?", "value": 200},
        {"question": "This president was never elected as president or vice president", "answer": "Who is Gerald Ford?", "value": 300},
    ],
    "First Ladies": [
        {"question": "She was the youngest First Lady at age 21", "answer": "Who is Frances Cleveland?", "value": 100},
        {"question": "This First Lady created the 'Just Say No' campaign", "answer": "Who is Nancy Reagan?", "value": 200},
        {"question": "She was the first First Lady to have a graduate degree", "answer": "Who is Hillary Clinton?", "value": 300},
    ]
}

SPORTS_QUESTIONS = {
    "Baseball": [
        {"question": "This player holds the MLB record for career home runs", "answer": "Who is Barry Bonds?", "value": 100},
        {"question": "This team broke the 'Curse of the Bambino' in 2004", "answer": "Who are the Boston Red Sox?", "value": 200},
        {"question": "He was the first player to break the color barrier in MLB", "answer": "Who is Jackie Robinson?", "value": 300},
    ],
    "Basketball": [
        {"question": "This NBA team won the most championships in the 1990s", "answer": "Who are the Chicago Bulls?", "value": 100},
        {"question": "He holds the record for most points in a single NBA game", "answer": "Who is Wilt Chamberlain?", "value": 200},
        {"question": "This player is known as 'King James'", "answer": "Who is LeBron James?", "value": 300},
    ]
}

MUSIC_QUESTIONS = {
    "Pop Music": [
        {"question": "This artist's 'Thriller' is the best-selling album of all time", "answer": "Who is Michael Jackson?", "value": 100},
        {"question": "She became the first female artist to win Album of the Year twice at the Grammys", "answer": "Who is Taylor Swift?", "value": 200},
        {"question": "This group from Liverpool changed pop music forever", "answer": "Who are The Beatles?", "value": 300},
    ],
    "Classical": [
        {"question": "This composer wrote 'Symphony No. 5' while becoming deaf", "answer": "Who is Beethoven?", "value": 100},
        {"question": "He composed 'The Four Seasons'", "answer": "Who is Vivaldi?", "value": 200},
        {"question": "This child prodigy composed his first piece at age 5", "answer": "Who is Mozart?", "value": 300},
    ]
}



class JeopardyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeopardy Game")
        self.root.geometry("800x600")
        self.score = 0
        self.questions = None

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
        self.mode_frame.pack_forget()

        # Set questions based on mode
        if mode == "Presidents":
            self.questions = PRESIDENT_QUESTIONS
        elif mode == "Sports":
            self.questions = SPORTS_QUESTIONS
        else:
            self.questions = MUSIC_QUESTIONS

        self.create_game_board()

    def create_game_board(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(expand=True, fill='both')

        # Create score display
        self.score_label = tk.Label(
            self.game_frame,
            text=f"Score: ${self.score}",
            font=("Arial", 20, "bold")
        )
        self.score_label.pack(pady=10)

        # Create game board grid
        self.board_frame = tk.Frame(self.game_frame)
        self.board_frame.pack(padx=20, pady=20)

        # Create category headers
        for col, category in enumerate(self.questions.keys()):
            tk.Label(
                self.board_frame,
                text=category,
                font=("Arial", 12, "bold"),
                wraplength=150,
                width=15,
                height=2,
                relief="raised"
            ).grid(row=0, column=col, padx=2, pady=2)

        # Create question buttons
        for col, category in enumerate(self.questions.keys()):
            for row, question in enumerate(self.questions[category], 1):
                btn = tk.Button(
                    self.board_frame,
                    text=f"${question['value']}",
                    width=15,
                    height=2,
                    command=lambda c=category, r=row-1: self.show_question(c, r)
                )
                btn.grid(row=row, column=col, padx=2, pady=2)

    def show_question(self, category, index):
        question = self.questions[category][index]
        response = messagebox.askquestion(
            "Question",
            question['question'],
            icon='question'
        )

        # Show answer and update score
        if response == 'yes':
            answer_correct = messagebox.askquestion(
                "Answer",
                f"The correct answer is: {question['answer']}\nDid you get it right?"
            )
            if answer_correct == 'yes':
                self.score += question['value']
            else:
                self.score -= question['value']

            # Update score display
            self.score_label.config(text=f"Score: ${self.score}")

            # Disable the button after it's been used
            for widget in self.board_frame.winfo_children():
                if widget.grid_info()['column'] == list(self.questions.keys()).index(category) \
                   and widget.grid_info()['row'] == index + 1:
                    widget.config(state='disabled', bg='gray')
        

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = JeopardyGame(root)
    root.mainloop()
