import math, random
from tkinter import ttk


moveList = ["U", "U'", "F", "F'", "R", "R'", "L", "L'", "B", "B'", "D", "D'"]
output = []

def scramble(moves):
    for i in range(moves):
              