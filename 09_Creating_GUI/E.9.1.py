import tkinter as tk

window = tk.Tk()


def enter_name():
    entry = field_1.get()
    result['text'] = 'Hello, ' + entry


text_1 = tk.Label(window, text='Enter name')
field_1 = tk.Entry(window)
button = tk.Button(window, text='Confirm', command=enter_name)
result = tk.Label(window, text="")

text_1.grid(row=0, column=0)
field_1.grid(row=0, column=1)
button.grid(row=0, column=2)
result.grid(row=1, columnspan=3)

window.mainloop()