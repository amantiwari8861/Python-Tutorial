#!/usr/bin/python3
# progressbar_scale.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)
progressbar.pack()

progressbar.config(mode = 'indeterminate')
progressbar.start()
progressbar.stop()

progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)
progressbar.config(value = 8.0)
progressbar.step()
progressbar.step(5)

value = DoubleVar()
progressbar.config(variable = value)

scale = ttk.Scale(root, orient = HORIZONTAL,
		  length = 400, variable = value,
		  from_ = 0.0, to = 11.0)
scale.pack()
scale.set(4.2)
print(scale.get())

root.mainloop()
