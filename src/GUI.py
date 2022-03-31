from tkinter import *
from time import *

class PuzzleSquare:
    def __init__(self, canvas, x, y, width, height, number):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.number = number
        self.color = "white"
        self.draw_square()
        self.draw_number()

    def draw_square(self):
        self.canvas.create_rectangle(self.x, self.y, self.x+self.width, self.y+self.height, fill=self.color)
    
    def draw_number(self):
        self.canvas.create_text(self.x+self.width/2, self.y+self.height/2, text=self.number, fill="black")
    

window = Tk()

width = 500
height = 500

canvas = Canvas(window, width=width, height=height)
canvas.pack()

number_1 = PuzzleSquare(canvas, 0, 0, width/4, height/4, 1)

coord = 10, 50, 240, 210


window.mainloop()


