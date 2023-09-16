from tkinter import *
import random
import pandas as pd


#-------------------------------- CONSTENTS AND FILES ------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
card_value = {}
df = pd.read_csv("data/french_words.csv")
word_dict = df.to_dict(orient = "records")

#-------------------------------- NEXT CARD FUNC ------------------------------------#

def next_card():
    global card_value,flip_timer
    card_value = random.choice(word_dict)
    window.after_cancel(flip_timer)
    french_word = card_value["French"]
    canvas_main.itemconfig(card_title, text = "French", fill = "black")
    canvas_main.itemconfig(card_word, text = french_word , fill = "black")
    canvas_main.itemconfig(card_background , image = frnt_img)
    flip_timer = window.after(2000, func= flip_card)

#-------------------------------- FLIP FUNC ------------------------------------#
def flip_card():
    english_word = card_value["English"]
    canvas_main.itemconfig(card_title , text = "English" ,fill = "white")
    canvas_main.itemconfig(card_word, text = english_word, fill = "white")
    canvas_main.itemconfig(card_background, image = back_img)
    


#-------------------------------- UI DESIGN ------------------------------------#


window = Tk()
window.title('Flash Card' )
window.config(padx=50, pady=50 , background=BACKGROUND_COLOR)

flip_timer = window.after(2000, func= flip_card)

frnt_img = PhotoImage(file = "images/card_front.png")
back_img = PhotoImage(file = "images/card_back.png")
canvas_main = Canvas(width=800, height=526)
card_background = canvas_main.create_image(400,263 , image = frnt_img)
canvas_main.config(bg=BACKGROUND_COLOR , highlightthickness=0)
card_title = canvas_main.create_text(400, 150 , text = "title" , font = ('Ariel', 40, 'italic'))
card_word = canvas_main.create_text(400, 236 , text = "word" , font = ('Ariel', 60, 'bold'))
canvas_main.grid(row=0 , column=0 , columnspan=2)


cross_btn_img = PhotoImage(file = "images/wrong.png")
cross_btn = Button(image=cross_btn_img , highlightthickness=0 , command=next_card)
cross_btn.grid(row=1 , column=0)

check_btn_img = PhotoImage(file = "images/right.png")
check_btn = Button(image=check_btn_img , highlightthickness=0 , command=next_card)
check_btn.grid(row=1 , column=1)


next_card()
















window.mainloop()