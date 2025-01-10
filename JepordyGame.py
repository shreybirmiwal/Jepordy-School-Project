import tkinter as tk
from tkinter import messagebox
import pygame.mixer

# Initialize pygame mixer for sounds
pygame.mixer.init()

# Sound effects dictionary
SOUNDS = {
    'correct': 'correct.wav',
    'wrong': 'wrong.wav',
    'select': 'select.wav',
    'start': 'start.wav'
}

# Question databases
PRESIDENT_QUESTIONS = {
    "Early Presidents": [
        {
            "question":
            "This president was the first to live in the White House",
            "answer": "Who is John Adams?",
            "value": 100
        },
        {
            "question": "He was known as the 'Father of the Constitution'",
            "answer": "Who is James Madison?",
            "value": 200
        },
        {
            "question":
            "This president served the shortest term of only 31 days",
            "answer": "Who is William Henry Harrison?",
            "value": 300
        },
        {
            "question": "He purchased the Louisiana Territory",
            "answer": "Who is Thomas Jefferson?",
            "value": 400
        },
        {
            "question":
            "This president never married and was a lifelong bachelor",
            "answer": "Who is James Buchanan?",
            "value": 500
        },
    ],
    "20th Century": [
        {
            "question": "He was the first president to appear on television",
            "answer": "Who is Franklin D. Roosevelt?",
            "value": 100
        },
        {
            "question": "This president established NASA",
            "answer": "Who is Dwight D. Eisenhower?",
            "value": 200
        },
        {
            "question": "He was the only president to resign from office",
            "answer": "Who is Richard Nixon?",
            "value": 300
        },
        {
            "question": "This president was a former actor",
            "answer": "Who is Ronald Reagan?",
            "value": 400
        },
        {
            "question": "He served as president during World War I",
            "answer": "Who is Woodrow Wilson?",
            "value": 500
        },
    ],
    "Presidential Facts": [
        {
            "question": "This president was left-handed",
            "answer": "Who is Barack Obama?",
            "value": 100
        },
        {
            "question": "He was the youngest president at age 42",
            "answer": "Who is Theodore Roosevelt?",
            "value": 200
        },
        {
            "question": "This president won a Grammy Award",
            "answer": "Who is Bill Clinton?",
            "value": 300
        },
        {
            "question":
            "He was the first president born outside the original 13 colonies",
            "answer": "Who is Abraham Lincoln?",
            "value": 400
        },
        {
            "question":
            "This president installed the first White House swimming pool",
            "answer": "Who is Franklin D. Roosevelt?",
            "value": 500
        },
    ]
}

SPORTS_QUESTIONS = {
    "Baseball": [
        {
            "question":
            "This player holds the MLB record for career home runs",
            "answer": "Who is Barry Bonds?",
            "value": 100
        },
        {
            "question": "He had a 56-game hitting streak in 1941",
            "answer": "Who is Joe DiMaggio?",
            "value": 200
        },
        {
            "question": "This pitcher threw seven no-hitters",
            "answer": "Who is Nolan Ryan?",
            "value": 300
        },
        {
            "question": "He was known as 'The Great Bambino'",
            "answer": "Who is Babe Ruth?",
            "value": 400
        },
        {
            "question": "This team won the first World Series in 1903",
            "answer": "Who are the Boston Americans?",
            "value": 500
        },
    ],
    "Basketball": [
        {
            "question":
            "This NBA team won the most championships in the 1990s",
            "answer": "Who are the Chicago Bulls?",
            "value": 100
        },
        {
            "question": "He scored 100 points in a single game",
            "answer": "Who is Wilt Chamberlain?",
            "value": 200
        },
        {
            "question": "This team has the most NBA championships",
            "answer": "Who are the Boston Celtics?",
            "value": 300
        },
        {
            "question": "He was known as 'Pistol Pete'",
            "answer": "Who is Pete Maravich?",
            "value": 400
        },
        {
            "question": "This player won 11 NBA championships",
            "answer": "Who is Bill Russell?",
            "value": 500
        },
    ],
    "Olympics": [
        {
            "question": "This swimmer has the most Olympic medals",
            "answer": "Who is Michael Phelps?",
            "value": 100
        },
        {
            "question": "She won four gold medals in gymnastics in 1984",
            "answer": "Who is Mary Lou Retton?",
            "value": 200
        },
        {
            "question": "This country hosted the first modern Olympics",
            "answer": "What is Greece?",
            "value": 300
        },
        {
            "question":
            "He set the long jump record in 1968 that stood for 23 years",
            "answer": "Who is Bob Beamon?",
            "value": 400
        },
        {
            "question": "This sprinter won gold in four consecutive Olympics",
            "answer": "Who is Carl Lewis?",
            "value": 500
        },
    ]
}

MUSIC_QUESTIONS = {
    "Rock Legends": [
        {
            "question": "This band's debut album was 'Please Please Me'",
            "answer": "Who are The Beatles?",
            "value": 100
        },
        {
            "question": "He was known as 'The King of Rock and Roll'",
            "answer": "Who is Elvis Presley?",
            "value": 200
        },
        {
            "question": "This band wrote 'Stairway to Heaven'",
            "answer": "Who is Led Zeppelin?",
            "value": 300
        },
        {
            "question": "He was the lead singer of Queen",
            "answer": "Who is Freddie Mercury?",
            "value": 400
        },
        {
            "question":
            "This guitarist played a flaming guitar at Monterey Pop",
            "answer": "Who is Jimi Hendrix?",
            "value": 500
        },
    ],
    "Modern Music": [
        {
            "question":
            "This artist's 'Folklore' won Album of the Year in 2021",
            "answer": "Who is Taylor Swift?",
            "value": 100
        },
        {
            "question": "He is known as the 'King of Pop'",
            "answer": "Who is Michael Jackson?",
            "value": 200
        },
        {
            "question": "This rapper's first hit was 'Through the Wire'",
            "answer": "Who is Kanye West?",
            "value": 300
        },
        {
            "question":
            "She became the youngest person to win Album of the Year",
            "answer": "Who is Billie Eilish?",
            "value": 400
        },
        {
            "question": "This artist has won the most Grammy Awards",
            "answer": "Who is Georg Solti?",
            "value": 500
        },
    ],
    "Music History": [
        {
            "question": "This instrument was invented by Adolphe Sax",
            "answer": "What is the Saxophone?",
            "value": 100
        },
        {
            "question": "This composer wrote 'The Four Seasons'",
            "answer": "Who is Vivaldi?",
            "value": 200
        },
        {
            "question": "This style of music originated in New Orleans",
            "answer": "What is Jazz?",
            "value": 300
        },
        {
            "question": "This device replaced the 8-track tape",
            "answer": "What is the Cassette?",
            "value": 400
        },
        {
            "question": "This composer wrote his first symphony at age 8",
            "answer": "Who is Mozart?",
            "value": 500
        },
    ]
}


class JeopardyGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Jeopardy Game")
        self.root.geometry("1024x768")
        self.score = 0
        self.game_time = 0
        self.game_timer = None
        self.time_label = None

        self.create_main_menu()

    def play_sound(self, sound_type):
        try:
            pygame.mixer.Sound(SOUNDS[sound_type]).play()
        except:
            pass

    def create_main_menu(self):
        self.main_menu = tk.Frame(self.root, bg='navy')
        self.main_menu.pack(expand=True, fill='both')

        self.title_label = tk.Label(self.main_menu,
                                    text="JEOPARDY",
                                    font=("Arial", 48, "bold"),
                                    fg="yellow",
                                    bg='navy')
        self.title_label.pack(pady=50)

        self.start_button = tk.Button(self.main_menu,
                                      text="Start Game",
                                      font=("Arial", 20),
                                      command=self.show_game_modes,
                                      width=15,
                                      height=2,
                                      bg='gold',
                                      fg='navy')
        self.start_button.pack(pady=30)

    def update_game_timer(self):
        self.game_time += 1
        minutes = self.game_time // 60
        seconds = self.game_time % 60
        self.time_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
        self.game_timer = self.root.after(1000, self.update_game_timer)

    def start_game_timer(self):
        if self.time_label is None:
            self.time_label = tk.Label(self.game_frame,
                                       text="Time: 00:00",
                                       font=("Arial", 24, "bold"),
                                       fg="yellow",
                                       bg='navy')
            self.time_label.pack(pady=5)
        self.update_game_timer()

    def stop_game_timer(self):
        if self.game_timer:
            self.root.after_cancel(self.game_timer)
            self.game_timer = None

    def show_game_modes(self):
        self.play_sound('select')
        self.main_menu.pack_forget()

        self.mode_frame = tk.Frame(self.root, bg='navy')
        self.mode_frame.pack(expand=True, fill='both')

        mode_label = tk.Label(self.mode_frame,
                              text="Select Game Mode",
                              font=("Arial", 36, "bold"),
                              fg="yellow",
                              bg='navy')
        mode_label.pack(pady=30)

        modes = {
            "Presidents": PRESIDENT_QUESTIONS,
            "Sports": SPORTS_QUESTIONS,
            "Music": MUSIC_QUESTIONS
        }

        for mode, questions in modes.items():
            button = tk.Button(
                self.mode_frame,
                text=mode,
                font=("Arial", 18),
                width=15,
                height=2,
                command=lambda m=mode, q=questions: self.start_game(m, q),
                bg='gold',
                fg='navy')
            button.pack(pady=10)

        back_button = tk.Button(self.mode_frame,
                                text="Back to Main Menu",
                                font=("Arial", 14),
                                command=self.return_to_main,
                                bg='red',
                                fg='white')
        back_button.pack(pady=20)

    def start_game(self, mode, questions):
        self.play_sound('start')
        self.mode_frame.pack_forget()
        self.questions = questions
        self.game_time = 0  # Reset timer

        self.game_frame = tk.Frame(self.root, bg='navy')
        self.game_frame.pack(expand=True, fill='both')

        # Score and timer display
        score_frame = tk.Frame(self.game_frame, bg='navy')
        score_frame.pack(pady=10)

        self.score_label = tk.Label(
            score_frame,
            text=f"Score: ${self.score}",
            font=("Arial", 24, "bold"),
            fg="yellow",
            bg='navy'
        )
        self.score_label.pack(side='left', padx=20)

        # Start the game timer
        self.start_game_timer()

        # Game board
        self.board_frame = tk.Frame(self.game_frame, bg='navy')
        self.board_frame.pack(pady=20)

        # Create category headers
        for col, category in enumerate(questions.keys()):
            tk.Label(self.board_frame,
                     text=category,
                     font=("Arial", 12, "bold"),
                     wraplength=150,
                     height=2,
                     width=20,
                     relief='raised',
                     bg='navy',
                     fg='yellow').grid(row=0, column=col, padx=5, pady=5)

        # Create question buttons
        for col, category in enumerate(questions.keys()):
            for row, question in enumerate(questions[category]):
                btn = tk.Button(
                    self.board_frame,
                    text=f"${question['value']}",
                    width=20,
                    height=2,
                    command=lambda c=category, r=row: self.show_question(c, r),
                    bg='gold',
                    fg='navy')
                btn.grid(row=row + 1, column=col, padx=5, pady=5)

        # Back button
        back_button = tk.Button(self.game_frame,
                                text="Back to Game Modes",
                                font=("Arial", 14),
                                command=self.return_to_modes,
                                bg='red',
                                fg='white')
        back_button.pack(pady=10)

    def show_question(self, category, index):
        self.play_sound('select')
        question = self.questions[category][index]
        response = messagebox.askquestion("Question",
                                          question['question'],
                                          icon='question')

        if response == 'yes':
            answer_correct = messagebox.askquestion(
                "Answer",
                f"The correct answer is: {question['answer']}\nDid you get it right?"
            )
            if answer_correct == 'yes':
                self.play_sound('correct')
                self.score += question['value']
            else:
                self.play_sound('wrong')
                self.score -= question['value']

            self.score_label.config(text=f"Score: ${self.score}")

            # Disable used question
            for widget in self.board_frame.winfo_children():
                if widget.grid_info()['column'] == list(self.questions.keys()).index(category) \
                   and widget.grid_info()['row'] == index + 1:
                    widget.config(state='disabled', bg='gray')

    def return_to_main(self):
        self.play_sound('select')
        self.stop_game_timer()

        if hasattr(self, 'mode_frame'):
            self.mode_frame.pack_forget()
        if hasattr(self, 'game_frame'):
            self.game_frame.pack_forget()
        self.create_main_menu()

    def return_to_modes(self):
        self.stop_game_timer()

        self.play_sound('select')
        self.score = 0
        self.game_frame.pack_forget()
        self.show_game_modes()


if __name__ == "__main__":
    root = tk.Tk()
    game = JeopardyGame(root)
    root.mainloop()
