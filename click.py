from math import *
from random import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from imageImports import *
root = tk.Tk()
style = ttk.Style()
maincanvas = tk.Canvas(root, width=450, height=300)
maincanvas.pack()
total = 0
pbMoving = True

def progress():
    if pb['value'] < 100:
        pb['value'] += 1 
        if(pb['value'] % 10 == 0):
            pass
        else: 
            progress()
    else:
        pb['value'] = 0

style.configure("bar.Horizontal.TProgressBar",
            background="#f7d272"
            
)

mainlabel = tk.Label(root, textvariable=str(total))    
maincanvas.create_window(175, 150, window=mainlabel)

incrementor = tk.Button(text= 'click', command=progress)
maincanvas.create_window(225, 30, window=incrementor)

pb = ttk.Progressbar(root, style="bar.Horizontal.TProgressbar", mode='determinate', length=200, orient='horizontal')
maincanvas.create_window(100, 30, window=pb)

root.mainloop()