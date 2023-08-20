from tkinter import *
CONVERSION_FACTOR = 1.60934


def miles_to_km(miles):
    kilometers = miles * CONVERSION_FACTOR
    return kilometers


def km_to_miles(km):
    miles = km / CONVERSION_FACTOR
    return miles


# function to clear
def button_cl():
    user_input.delete(0, END)
    result_label.config(text="0")
    input_label.config(text="Conversion Program")


# function to exit the program
def exit_program():
    window.destroy()


# create spinbox function
def spinbox_clicked():
    user_val = float(user_input.get())
    if spinbox.get() == "Miles":
        get_val = miles_to_km(user_val)
        output_unit = "Km"
    else:
        get_val = km_to_miles(user_val)
        output_unit = "Miles"

    result_label.config(text="{:.2f}".format(get_val))
    output_label.config(text='Miles')
    input_label.config(text=f'Conversion {spinbox.get()} to {output_unit}')


# --------------CREATE A WINDOW-----------------------
window = Tk()
window.title("Miles-Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100,)


# CREATE A LABEL FOR ENTRY
user_input = Entry()
user_input.grid(row=2, column=1)
user_input.focus()


# CREATE A LABEL FOR RESULTS
result_label = Label(text="0", font=('Arial', 12, 'bold'),)
result_label.grid(row=2, column=3)
result_label.config(padx=10, pady=10)

# CREATE A LABEL FOR USER INPUT
input_label = Label(text="Conversion Program", width=20, font=('Arial', 12, 'bold'))
input_label.grid(row=1, column=2)

# CREATE A LABEL FOR TITLE
output_label = Label(text="", width=10, font=('Arial', 12, 'bold'))
output_label.grid(row=2, column=4)
output_label.config(padx=50, pady=50)
# CREATE A SPINBOX FOR USER INPUT
unit_choices = ("Km", "Miles")
spinbox = Spinbox(values=unit_choices, width=10, command=spinbox_clicked)
spinbox.grid(row=2, column=2)

# CREATE A BUTTON TO EXIT
button_exited = Button(text="Exit", command=exit_program, bg="red", fg="black")
button_exited.grid(row=3, column=3)
# CREATE A BUTTON TO CLEAR
button_clear = Button(text="Clear", command=button_cl, bg="green", fg="black")
button_clear.grid(row=3, column=1)

# keep window appear on the screen
window.mainloop()
