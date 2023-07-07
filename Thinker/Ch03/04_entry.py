#!/usr/bin/python3
# entry.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root, width = 30)
entry.pack()

entry.get()
entry.delete(0, 1)
entry.delete(0, END)
entry.insert(0, 'Enter your password')

entry.config(show = '*')
entry.state(['disabled'])
entry.state(['readonly'])
entry.state(['!disabled'])

root.mainloop()
