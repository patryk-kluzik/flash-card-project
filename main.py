from tkinter import *

# ------------------------------------------- CONSTANTS -------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")

# ----------------------------------------------- UI -----------------------------------------------#
window = Tk()
window.title("Polish to English Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
flashcard = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=flashcard)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
language_canvas = canvas.create_text(400, 150, text="Polish", fill="black", font=FONT_LANGUAGE)
word_canvas = canvas.create_text(400, 263, text="chlopiec", fill="black", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

# BUTTONS
wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image)
wrong_button.config(padx=50, highlightthickness=0, bd=0,)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image)
right_button.config(padx=50, highlightthickness=0, bd=0)
right_button.grid(column=1, row=1)

window.mainloop()
