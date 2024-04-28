from tkinter import *
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

window = Tk()
window.geometry("420x420")
window.title("Chatting App")
# print(os.getcwd())  # Print the current working directory
# icon = PhotoImage(file='./Tkinter/logo.png')
# window.iconphoto(True, icon)
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

# inp=Entry(window,font=("Arial",50))
# inp.pack()
# def submit():
#     text=inp.get()
#     print("Text:",text)
# submit_btn=Button(window,text="submit",command=submit)
# submit_btn.pack(side=RIGHT)
window.mainloop()
