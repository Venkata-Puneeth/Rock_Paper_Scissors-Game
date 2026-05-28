import customtkinter as ctk
import random

# ---------------- CONFIG ----------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0


# ---------------- GAME LOGIC ----------------
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.configure(text=f"You chose: {user_choice}")
    computer_label.configure(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie 🤝"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "You Win 🎉"
        user_score += 1
    else:
        result = "You Lose 😢"
        computer_score += 1

    result_label.configure(text=result)
    score_label.configure(text=f"Score → You: {user_score} | Computer: {computer_score}")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.configure(text="Score → You: 0 | Computer: 0")
    result_label.configure(text="")
    user_label.configure(text="")
    computer_label.configure(text="")


# ---------------- UI ----------------
app = ctk.CTk()
app.title("Rock Paper Scissors")
app.geometry("500x500")

# Title
title = ctk.CTkLabel(app, text="✊ Rock Paper Scissors ✋",
                     font=("Segoe UI", 22, "bold"))
title.pack(pady=15)

# Instructions
instruction = ctk.CTkLabel(app, text="Choose one option to play",
                           text_color="gray")
instruction.pack()

# Buttons
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=20)

ctk.CTkButton(btn_frame, text="🪨 Rock", width=120,
              command=lambda: play("Rock")).grid(row=0, column=0, padx=10)

ctk.CTkButton(btn_frame, text="📄 Paper", width=120,
              command=lambda: play("Paper")).grid(row=0, column=1, padx=10)

ctk.CTkButton(btn_frame, text="✂️ Scissors", width=120,
              command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# Result display
user_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 12))
user_label.pack()

computer_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 12))
computer_label.pack()

result_label = ctk.CTkLabel(app, text="", font=("Segoe UI", 18, "bold"))
result_label.pack(pady=10)

# Score
score_label = ctk.CTkLabel(app, text="Score → You: 0 | Computer: 0",
                           font=("Segoe UI", 12))
score_label.pack(pady=5)

# Reset button
reset_btn = ctk.CTkButton(app, text="Reset Game", command=reset_game)
reset_btn.pack(pady=15)

app.mainloop()