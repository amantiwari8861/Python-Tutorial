#!/usr/bin/python3
# pack.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
label = ttk.Label(root, text = 'Hello, Tkinter!',
          background = 'green')
label.pack(side = LEFT, ipadx = 10, ipady = 10)
print(label)

for widget in root.pack_slaves():
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())

label.pack_forget()

root.mainloop()
