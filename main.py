from tkinter import *
import pandas
from random import choice

# data is a dataframe object
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/polish_to_english.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")
# convert to dictionary

current_card = {}


def next_word():
    print(len(words_to_learn))
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_to_learn)
    canvas.itemconfig(language_canvas, text="Polish", fill="black")
    canvas.itemconfig(word_canvas, text=current_card["polish"], fill="black")
    canvas.itemconfig(card_background, image=card_front)

    flip_timer = window.after(3000, flip_flashcard)

def knows_word():
    words_to_learn.remove(current_card)

    remaining_words = pandas.DataFrame(words_to_learn)
    remaining_words.to_csv("./data/words_to_learn.csv", index=False)

    next_word()


def flip_flashcard():
    canvas.itemconfig(language_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=current_card["english"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


# ------------------------------------------- CONSTANTS -------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

# ----------------------------------------------- UI -----------------------------------------------#
window = Tk()
window.title("Polish to English Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_flashcard)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
language_canvas = canvas.create_text(400, 150, fill="black", font=FONT_LANGUAGE)
word_canvas = canvas.create_text(400, 263, fill="black", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image)
wrong_button.config(padx=50, highlightthickness=0, bd=0, command=next_word)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image)
right_button.config(padx=50, highlightthickness=0, bd=0, command=knows_word)
right_button.grid(column=1, row=1)

next_word()

window.mainloop()
