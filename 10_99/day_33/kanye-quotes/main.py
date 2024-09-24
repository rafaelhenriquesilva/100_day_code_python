from pathlib import Path
from tkinter import *
import requests

def get_quote():
    data = requests.get('https://api.kanye.rest')
    data = data.json()
    try:
        canvas.itemconfig(quote_text, text=data['quote'])
    except:
        raise Exception('Error to request')

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_file_path = Path(__file__).parent / "background.png" 
background_img = PhotoImage(file=background_file_path)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)
kanye_file_path = Path(__file__).parent / "kanye.png" 
kanye_img = PhotoImage(file=kanye_file_path)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()