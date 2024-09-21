from tkinter import *
from tkinter import messagebox
from pathlib import Path
from password_generator import GeneratePassword
import json
FONT=('Arial', 10)
# grid add - columnspan = 2 - Show in 2+ columns
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    aux = GeneratePassword()
    password = aux.exec()
    password_input.insert(0, f'{password}')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def verify_fields_to_save(website, email, password):
    is_valid = True
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        is_valid = False
        messagebox.showerror(
            title='Required Fields',
            message=f'Website, username and password are required'
        )
    return is_valid

def save():
    website = website_input.get()
    email = username_input.get()    
    password = password_input.get()

    is_valid = verify_fields_to_save(email=email,password=password, website=website)

    if(is_valid == False):
        return
    
    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n Email: {email} \n Password: {password}\n Is it ok to save?')

    if is_ok:
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        try:
            update_file(new_data)
        except FileNotFoundError:
            save_file(new_data)
        else:
            clear()

def clear():
    website_input.delete(0, 'end')
    username_input.delete(0, 'end')
    password_input.delete(0, 'end')
# ---------------------------- MANIPULATE JSON------------------------------- #
def save_file(new_data):
    file_path = Path(__file__).parent / "password_data.json"
    with open(file_path, "w") as data_file: 
        json.dump(new_data, data_file, indent=4)

def update_file(new_data):
    data = read_file()
    data.update(new_data)
    save_file(data)

def read_file():
    file_path = Path(__file__).parent / "password_data.json"
    with open(file_path, "r") as data_file: 
        data = json.load(data_file)
        return data
# ---------------------------- SEARCH BUTTON ------------------------------- #
def search():
    website = website_input.get()
    data = read_file()
    try:
        result = data[website]
        messagebox.showinfo(title=website, message=f"email:{result['email']}\n password:{result['password']}")
    except KeyError:
        messagebox.showerror(title='Not Found', message='Company not found')
    
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Password Image
# Put Image on Program
image_path = Path(__file__).parent / "password.png" 
password_img = PhotoImage(file=image_path)

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100,image=password_img)
canvas_image = canvas.create_text(200,200, fill="white", font=('Arial',35, 'bold'))
canvas.grid(column=1, row=0)

# Website Label and Input
website_label = Label(text='Website:', font=FONT)
website_label.grid(column=0,row=1)

# Search Button
search_button = Button(text='Search', width=12, command=search)
search_button.grid(column=2,row=1)

# Focus on Input
website_input = Entry(width=35)
website_input.grid(column=1,row=1)
website_input.focus()

# Username Label and Input
username_label = Label(text='Email/Username:', font=FONT)
username_label.grid(column=0,row=2)

username_input = Entry(width=35)
username_input.grid(column=1,row=2)

# Default Value
username_input.insert(0, 'rafael@gmail.com')

# Password Label and Input
password_label = Label(text='Email/Password:', font=FONT)
password_label.grid(column=0,row=3)

password_input = Entry(width=34)
password_input.grid(column=1,row=3)

# Generate Password Button
generate_password_button = Button(text='Generate Password', command=generate_pass)
generate_password_button.grid(column=2,row=3)


# Add Password Button
Add_password_button = Button(text='Add Password', width=36, command=save)
Add_password_button.grid(column=0,row=4, columnspan=4)

window.mainloop()