# ---------------------- PACKAGES ------------------------
# pip install pandas 
from tkinter import *
#from tkinter import messagebox
from pathlib import Path
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
ENGLISH_KEY = 'English'
FRENCH_KEY = 'French'
CARD_FRONT_IMAGE_PATH = "./images/card_front.png"
CARD_BACK_IMAGE_PATH = './images/card_back.png'
WRONG_IMAGE_PATH = './images/wrong.png'
RIGHT_IMAGE_PATH = './images/right.png'
current_card = {}

# --------------------------- READ FRENCH WORDS ---------------------------
def read_french_words():
    french_words_path = Path(__file__).parent / './data/french_words.csv'
    data = pandas.read_csv(french_words_path)
    # orient records transform in list of dictionaries
    to_learn = data.to_dict(orient='records')
    return to_learn
# --------------------------- UPDATE BACKGROUND IMAGE -----------------------
def update_canvas_background(image):
    canvas.itemconfig(card_background, image=image)

# --------------------------- NEXT CARD FUNCTION ---------------------------
def next_card(is_know: bool = False):
    global current_card
    # USE CARD FRONT IMAGE ON CANVAS
    update_canvas_background(card_front_img)

    to_learn = read_french_words()
    current_card = random.choice(to_learn)
    # item config to change specific item in canvas
    canvas.itemconfig(card_title, text=FRENCH_KEY, fill="black")
    canvas.itemconfig(card_word, text=current_card[FRENCH_KEY], fill="black")

    if(is_know):
        print('I know')
        print(current_card)

    fire_flip_card()
    
def is_know():
    next_card(TRUE)

# --------------------------- FLIP CARD FUNCTION ---------------------------
def flip_card():
    global current_card
    english_word = ''

    try:
        english_word = current_card[ENGLISH_KEY]
    except:
        english_word = 'Not Found'

    canvas.itemconfig(card_title, text=ENGLISH_KEY, fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")

    # USE CARD BACK IMAGE ON CANVAS
    update_canvas_background(card_back_img)
    
def fire_flip_card():
    # Window After, each a time defined to execute a funtion
    window.after(3000, func=flip_card)

# --------------------------- UI CONFIG ---------------------------
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card front image
# File path to search the file, start in way of code
card_front_path = Path(__file__).parent /  CARD_FRONT_IMAGE_PATH
card_front_img =  PhotoImage(file=card_front_path)
# Canvas to recipe the image and render on Tkinter
canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400,263,image=card_front_img)

# Card BACK image
# File path to search the file, start in way of code
card_back_path = Path(__file__).parent /  CARD_BACK_IMAGE_PATH
card_back_img =  PhotoImage(file=card_back_path)


# Canvas config add new styles to Object
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)

# text in canvas
card_title = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="word", font=('Ariel', 60, 'bold'))
# Grid to organize the item on Tkinter
canvas.grid(row=0, column=0, columnspan=2)

# Button Unknow with image
wrong_image_path = Path(__file__).parent / WRONG_IMAGE_PATH 
cross_image = PhotoImage(file=wrong_image_path)
unknow_bottom = Button(image=cross_image, highlightthickness=0, command=next_card)
unknow_bottom.grid(row=1,column=0)

# Button KNOW with image
know_image_path =  Path(__file__).parent / RIGHT_IMAGE_PATH
know_image = PhotoImage(file=know_image_path)
know_bottom = Button(image=know_image, highlightthickness=0, command=is_know)
know_bottom.grid(row=1, column=1)
window.mainloop()