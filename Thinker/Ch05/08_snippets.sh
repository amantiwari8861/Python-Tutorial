#!/usr/bin/python3
# scrollbar.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

text = Text(root, width = 40, height = 10, wrap = 'word')
text.grid(row = 0, column = 0)

# you can use this loop to populate the text
for i in range(1, 50):
    text.insert('end', 'line {}\n'.format(i))
	
scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview)
scrollbar.grid(row = 0, column = 1, sticky = 'ns')
text.config(yscrollcommand = scrollbar.set)