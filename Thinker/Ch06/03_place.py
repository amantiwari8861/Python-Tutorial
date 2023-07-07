#!/usr/bin/python3
# place.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()
root.geometry('640x480+200+200')

ttk.Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)
ttk.Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
ttk.Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
ttk.Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')

root.mainloop()
