from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Polish to English Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=30, pady=30)


canvas = Canvas(width=800, height=600)
flashcard = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,300, image=flashcard)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=1,row=0)



window.mainloop()