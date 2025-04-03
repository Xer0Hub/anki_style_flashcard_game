#--------------IMPORTS AND DEPENDENCIES--------------------#
from tkinter import *
import json as js
import pandas as pd
#---------------------UI SET UP---------------------------#
#CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
BACK_OF_CARD = "#91C2AF"

#VARIABLES

#DICTIONARY COUNTER
card_counter = 0

#WINDOW
window = Tk()
window.title("ANKI LITE")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.geometry("800x500")

#IMAGE LIBRARY
correct_img = PhotoImage(file="C:\\Users\\daniel.ginnane\\PycharmProjects\\Anki_Lite\\right.png")
incorrect_img = PhotoImage(file="C:\\Users\\daniel.ginnane\\PycharmProjects\\Anki_Lite\\wrong.png")
card_front_img = PhotoImage(file="C:\\Users\\daniel.ginnane\\PycharmProjects\\Anki_Lite\\card_front.png")
card_back_img = PhotoImage(file="C:\\Users\\daniel.ginnane\\PycharmProjects\\Anki_Lite\\card_back.png")

#--------------------FUNCTIONS AND DEFINITIONS------------------------------#
def incorrect_answer():
    #KEEP CARD IN DECK
    french_title.grid_remove()
    french_card.grid_remove()
    show_answer()

def correct_answer():
    #POP() CARD OUT OF LIST
    global card_counter
    card_counter += 1

    card_back_onscreen.grid_remove()

    french_title.grid_remove()
    french_card.grid_remove()
    card_back_onscreen.grid(column=0, row=0, columnspan=2)
    #TODO Make it so when I remove french title and card I can re-add it!


def show_answer():
    global card_counter

    card_front_onscreen = Label(image=card_front_img, bg=BACKGROUND_COLOR, highlightthickness=0, height=300, width=700)
    card_front_onscreen.grid(column=0, row=0, columnspan=2)

    english_title = Label(text="ENGLISH", font=("Arial", 15, "bold"), bg="white")
    english_title.grid(column=0, row=0, columnspan=2, sticky="n")

    english_card = Label(text=english_dict[card_counter], font=("Arial", 30, "bold"), bg="white")
    english_card.grid(column=0, row=0, columnspan=2)

#---------------------ON SCREEN ------------------------------------#
#ON SCREEN CARD
card_back_onscreen = Label(image=card_back_img, highlightthickness=0, height=300, width=700)
card_back_onscreen.grid(column=0, row=0, columnspan=2)

#WORD LIST TO DICTIONARY
french_list = pd.read_csv("french_words.csv")
word_dict = french_list.to_dict(orient='dict')
#ENGLISH DICT
english_dict = word_dict['English']
#FRENCH DICT
french_dict = word_dict['French']

#ENGLISH CARDS GET CALLED IN FUNCTION ONLY TO KEEP THEM CURRENT

#FRENCH CARDS
french_title = Label(text="FRENCH", font=("Arial", 15, "bold"), bg=BACK_OF_CARD)
french_title.grid(column=0, row=0, columnspan=2, sticky="n")

french_card = Label(text=french_dict[card_counter], font=("Arial", 30, "bold"), bg=BACK_OF_CARD)
french_card.grid(column=0, row=0, columnspan=2)

#BUTTONS
correct_button = Button(image=correct_img, highlightthickness=0, height=100, width=100, command=correct_answer)
correct_button.grid(column=1, row=1)

incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=incorrect_answer)
incorrect_button.grid(column=0, row=1)


















window.mainloop()






















