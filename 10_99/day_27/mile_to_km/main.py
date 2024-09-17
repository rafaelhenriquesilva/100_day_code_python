
import tkinter
FONT = ('Arial')
window = tkinter.Tk()
window.title('Mile to KM Converter')
window.config(padx=20, pady=20)


# Entry KM component
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1,row=0)

# Miles
miles_label = tkinter.Label(text='Miles', font=FONT)
miles_label.grid(column=2,row=0)

# Is Equal to
is_equal_to_label = tkinter.Label(text='is equal to', font=FONT)
is_equal_to_label.grid(column=0,row=1)

# km value
km_value_label = tkinter.Label(text='0', font=FONT)
km_value_label.grid(column=1,row=1)

# km label
km_label = tkinter.Label(text='KM', font=FONT)
km_label.grid(column=2,row=1)


# Button
def calculate_km_to_mile():
    miles = miles_input.get()
    km = round(float(miles) * 1.689)
    km_value_label.config(text=f"{km}")
button = tkinter.Button(text='Calculate', command=calculate_km_to_mile)
button.grid(column=1,row=2)

# Move Components - pack, place (x and y) and grid

# Stop the screen in program
window.mainloop()