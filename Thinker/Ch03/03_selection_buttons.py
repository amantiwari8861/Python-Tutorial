#!/usr/bin/python3
# selection_buttons.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

checkbutton = ttk.Checkbutton(root, text = 'SPAM?')
checkbutton.pack()

spam = StringVar()
spam.set('SPAM!')
print(spam.get())

checkbutton.config(variable = spam, onvalue = 'SPAM Please!',
		   offvalue = 'Boo SPAM!')
print(spam.get())

breakfast = StringVar()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast,
		value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast,
		value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()
print(breakfast.get()) # Note: value will be empty if no selection is made

checkbutton.config(textvariable = breakfast)

root.mainloop()
