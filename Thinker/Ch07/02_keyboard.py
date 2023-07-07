#!/usr/bin/python3
# keyboard.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        

def key_press(event):
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('char: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}\n'.format(event.keycode))

def shortcut(action):
    print(action)
    
root = Tk()

root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))

root.mainloop()
