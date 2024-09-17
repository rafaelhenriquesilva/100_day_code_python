# Introduction a Thinker
# GUI Interface
import tkinter

window = tkinter.Tk()
window.title('My First Gui Program')
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))

my_label.grid(column=0,row=0)

# Entry component
input = tkinter.Entry()
input.grid(column=0,row=1)

# Button
def button_clicked():
    value_input = input.get()
    my_label.config(text=value_input)
button = tkinter.Button(text='Click me', command=button_clicked)
button.grid(column=0,row=2)

# Move Components - pack, place (x and y) and grid

# Stop the screen in program
window.mainloop()