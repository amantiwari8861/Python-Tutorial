from tkinter import messagebox
from ttkbootstrap import *
from CRUD import *

main_window=Window(title="Main",scaling="2",resizable=(False,False))
main_window.geometry("600x600")

idLabel=Label(main_window,text="Enter Id:")
idEntry=Entry(font=('Arial'))
idLabel.grid(row=0,column=1)
idEntry.grid(row=0,column=2)

Label(main_window,text="Enter Name:").grid(row=1,column=1)
nameEntry=Entry(font=('Arial'))
nameEntry.grid(row=1,column=2)

Label(main_window,text="Enter Phone:").grid(row=2,column=1)
phoneEntry=Entry(font=('Arial'))
phoneEntry.grid(row=2,column=2)

Label(main_window,text="Enter Address:").grid(row=3,column=1)
addressEntry=Entry(font=('Arial'))
addressEntry.grid(row=3,column=2)

Label(main_window,text="Enter Fee:").grid(row=4,column=1)
feeEntry=Entry(font=('Arial'))
feeEntry.grid(row=4,column=2)

def insertData():
    print(idEntry.get())
    print(nameEntry.get())
    print(phoneEntry.get())
    print(addressEntry.get())
    print(feeEntry.get())
    insertOneRow(idEntry.get(),nameEntry.get(),phoneEntry.get(),addressEntry.get(),feeEntry.get())
    messagebox.showinfo(message="Data inserted succesfully!")
    main_window.destroy()

Button(text="Add Student!",bootstyle="SUCCESS",command=insertData).grid(columnspan=2,row=5,column=1)

main_window.mainloop()
