import tkinter as tk
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(text_title, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(text_title, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)   

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False) 
    next_card()


window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(width=800, height=526)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_image)
card_title = canvas.create_text(400, 150, text=f"French", font=("Ariel", 40, "italic"))
text_title = canvas.create_text(400, 263, text=f"{to_learn[0]["French"]}", font=("Ariel", 60, "bold"))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross_img, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)


tick_img = tk.PhotoImage(file="images/right.png")
tick_button = tk.Button(image=tick_img, highlightthickness=0, command=is_known)
tick_button.grid(column=1, row=1)

next_card()

window.mainloop()