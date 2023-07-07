#!/usr/bin/python3
# selection_boxes.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(month.get())
month.set('Dec')
month.set('Not a month!')

year = StringVar()
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()
print(year.get())

root.mainloop()
