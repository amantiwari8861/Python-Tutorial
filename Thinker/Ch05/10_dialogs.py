#!/usr/bin/python3
# dialogs.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import messagebox

messagebox.showinfo(title = "A Friendly Message", message = 'Hello, Tkinter!')
print(messagebox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?'))

from tkinter import filedialog
filename = filedialog.askopenfile()
print(filename.name)

from tkinter import colorchooser
print(colorchooser.askcolor(initialcolor = "#FFFFFF"))
