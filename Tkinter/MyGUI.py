from tkinter import Button, Entry, Label, PhotoImage, Tk, messagebox
import os
window=Tk()
window.geometry("460x460")
window.title("My Program")
# hello=Label(window,text="Hello World!",font=("Times New Roman",50))
# hello.pack()
# print(os.getcwd())
icon = PhotoImage(file='./Tkinter/logo2.png')
window.iconphoto(True, icon)
def showMsg():
    messagebox.showinfo(title="info",message="u clicked on add function")
    
num1=Label(window,text="Enter num1:",font=('Arial',40))
num2=Label(window,text="Enter num2:",font=('Arial',40))
input1=Entry(window,font=('Arial',40))
input2=Entry(window,font=('Arial',40))
add=Button(window,text="Add!!",font=('Arial',40),bg="#baff7a",command=showMsg)


for e in (num1,input1,num2,input2,add):
    e.pack()

window.mainloop()