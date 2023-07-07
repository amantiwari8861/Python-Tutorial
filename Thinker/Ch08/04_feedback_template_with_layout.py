#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

class Feedback:

    def __init__(self, master):    

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        self.logo = PhotoImage(file = 'tour_logo.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Thanks for Exploring!').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row = 1, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        
        ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        self.entry_name = ttk.Entry(self.frame_content, width = 24)
        self.entry_email = ttk.Entry(self.frame_content, width = 24)
        self.text_comments = Text(self.frame_content, width = 50, height = 10)

        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

        ttk.Button(self.frame_content, text = 'Submit').grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear').grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
