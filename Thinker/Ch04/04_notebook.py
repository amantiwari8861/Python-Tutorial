#!/usr/bin/python3
# notebook.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two')
ttk.Button(frame1, text = 'Click Me').pack()

frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text = 'Three')
notebook.forget(1)
notebook.add(frame3, text = 'Three')

print(notebook.select())
print(notebook.index(notebook.select()))
notebook.select(2)

notebook.tab(1, state = 'disabled')
notebook.tab(1, state = 'hidden')
notebook.tab(1, state = 'normal')
notebook.tab(1, 'text')
notebook.tab(1)

root.mainloop()
