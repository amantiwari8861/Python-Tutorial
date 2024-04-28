from tkinter import *
from tkinter import messagebox
# import os
# from PIL import Image, ImageTk

# count1=0

# def countr():
#     global count1
#     count1+=1
#     print("count=",count1)

# def sendMsg():
#     countr()
#     print("sending msg")

# def delete():
#     inp.delete(0,END)

window = Tk()
window.geometry("420x420")
window.title("Chatting App")
# print(os.getcwd())  # Print the current working directory
icon = PhotoImage(file='./Tkinter/logo.png')
window.iconphoto(True, icon)
# window.config(background="#000000")
# # photo=PhotoImage(file="./Tkinter/logo.png")

# image = Image.open('./Tkinter/logo.png')
# resized_image = image.resize((100, 100))
# photo = ImageTk.PhotoImage(resized_image)

# label = Label(window, text="Enter Text:", font=('Arial', 40, 'bold'), fg='green', bg="black",relief=RAISED, bd=10, padx=20, pady=20,image=photo) # type: ignore
# label.place(x=2, y=0)
# label.pack()

# button=Button(window,text="send",command=sendMsg,font=("Times New Roman",30),fg="#ffffff",bg="blue",activeforeground="blue",activebackground="white",image=photo,compound="right")
# button.pack()

# inp=Entry(window,font=("Arial",50),show="*")
# inp.pack()
# def submit():
#     text=inp.get()
#     print("Text:",text)
# submit_btn=Button(window,text="submit",command=submit)
# submit_btn.pack(side=RIGHT)
# x=IntVar()
# def desplay():
#     print(x.get())
# skill=Checkbutton(window,text="C",variable=x,onvalue=1,offvalue=0,command=desplay,compound="right")
# skill.pack()
genVal=StringVar()
def printGender():
    print(genVal.get())
gender=["Male","Female","others"]
for index in range(len(gender)):
    genRB=Radiobutton(window,text=index,variable=genVal,value=gender[index],command=printGender,padx=25,indicatoron=0,width=200)
    genRB.pack()
def click():
    # messagebox.showinfo(title="Info",message="good morning")
    # messagebox.showwarning(title="Info",message="good morning")
    # messagebox.showerror(title="Info",message="good morning")
    # status=messagebox.askokcancel(title="question",message="having lunch with me ?")
    # print(status)
    # parentWindow=Toplevel()
    # childWindow=Tk()
    window.destroy()

btn=Button(window,command=click,text="Click me!")
btn.pack()

window.mainloop()
