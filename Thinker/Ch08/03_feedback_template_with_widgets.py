#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

class Feedback:

    def __init__(self, master):    

        self.frame_header = ttk.Frame(master)
        
        self.logo = PhotoImage(file = 'tour_logo.gif')
        ttk.Label(self.frame_header, image = self.logo)
        ttk.Label(self.frame_header, text = 'Thanks for Exploring!')
        ttk.Label(self.frame_header, text = ("We're glad you chose Explore Californiafor your recent adventure.  "
                                             "Please tell us what you thought about the 'Desert to Sea' tour."))

        self.frame_content = ttk.Frame(master)

        ttk.Label(self.frame_content, text = 'Name:')
        ttk.Label(self.frame_content, text = 'Email:')
        ttk.Label(self.frame_content, text = 'Comments:')

        self.entry_name = ttk.Entry(self.frame_content, width = 24)
        self.entry_email = ttk.Entry(self.frame_content, width = 24)
        self.text_comments = Text(self.frame_content, width = 50, height = 10)

        ttk.Button(self.frame_content, text = 'Submit')
        ttk.Button(self.frame_content, text = 'Clear')

def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
