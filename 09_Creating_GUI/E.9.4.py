import tkinter as tk
from tkinter import SUNKEN, W, BOTTOM, X

window = tk.Tk()


def enter_name(event=None):
    entry = field_1.get()
    result['text'] = 'Hello, ' + entry + '!'


def clear():
    result['text'] = ''


def restore():
    return enter_name()


def exit_program():
    quit()


menu = tk.Menu(window)
window.config(menu=menu)
submenu = tk.Menu(menu, tearoff=0)

menu.add_cascade(label='Menu', menu=submenu)
submenu.add_command(label='Clear', command=clear)
submenu.add_command(label='Restore', command=restore)
submenu.add_separator()
submenu.add_command(label='Exit', command=exit_program)

text_1 = tk.Label(window, text='Enter name')
field_1 = tk.Entry(window)
button = tk.Button(window, text='Confirm', command=enter_name)
window.bind('<Return>', lambda event: enter_name())
result = tk.Label(window, text="")

text_1.grid(row=0, column=0)
field_1.grid(row=0, column=1)
button.grid(row=0, column=2)
result.grid(row=1, columnspan=3)

status_frame = tk.Frame(window, relief=SUNKEN, borderwidth=1)
status_frame.pack(side=BOTTOM, fill=X)
status = tk.Label(status_frame, text='Created', anchor=W)
status.pack(fill=X)
window.mainloop()