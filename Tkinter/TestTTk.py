import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# root = tk.Tk()
root = ttk.Window(themename="solar")
root.geometry("460x460")
root.title("Test TTK")

b1 = ttk.Button(root, text="Button 1", bootstyle=DANGER)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

ttk.DateEntry(bootstyle="success").pack()
# default Treeview style
ttk.Treeview().pack()

# info colored treeview style
ttk.Treeview(bootstyle='info').pack()


root.mainloop()