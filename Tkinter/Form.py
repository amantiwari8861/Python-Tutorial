from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
print(os.getcwd())  # Print the current working directory

# old_window=Tk()
old_window=ttk.Window(themename="solar",iconphoto='Tkinter/logo.png',resizable=(False,False),scaling=2)
old_window.geometry("720x460")
old_window.title("Chatting App")
icon=PhotoImage(file="./Tkinter/logo.png")
ico = icon.subsample(5, 5)

old_window.iconphoto(True,ico)

firstNameLabel=Label(old_window,text="First Name:",width=30).grid(row=0,column=0)
firstNameEntry=Entry(old_window,width=30).grid(row=0,column=1,padx=(1,50))
lastNameLabel=Label(old_window,text="last Name:").grid(row=1,column=0)
lastNameEntry=Entry(old_window).grid(row=1,column=1)
emailLabel=Label(old_window,text="Email:").grid(row=2,column=0)
emailEntry=Entry(old_window).grid(row=2,column=1,padx=(10,30),pady=(15,25))

submitBtn=Button(old_window,text="submit").grid(row=3,column=0,columnspan=2)

ttk.DateEntry()

# success colored date entry
ttk.DateEntry(bootstyle="success").grid(row=4,column=0)
root = ttk.Window(themename="solar")
root.mainloop()
old_window.mainloop()