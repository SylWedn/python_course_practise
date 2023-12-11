from calendar import isleap
import tkinter as tk

window = tk.Tk()


def enter_year():
    entry = int(field_1.get())
    if isleap(entry):
        result['text'] = str(entry) + ' is leap year!'
    else:
        result['text'] = str(entry) + ' is not leap year!'


text_1 = tk.Label(window, text='Enter year')
field_1 = tk.Entry(window)
button = tk.Button(window, text='Confirm', command=enter_year)
result = tk.Label(window, text="")

text_1.grid(row=0, column=0)
field_1.grid(row=0, column=1)
button.grid(row=0, column=2)
result.grid(row=1, columnspan=3)

window.mainloop()