from tkinter import *
from time import *
from PuzzleRoot import PuzzleRoot

window = Tk()
window.title("15-Puzzle Solver")
window.resizable(width=False, height=False)
window.configure(background='#fbf8f3')
width = 400
height = 400

space = Label(text="", background='#fbf8f3')
space.pack(side="top")

label = Label(text="15-Puzzle Steps Replayer", font=("Courier New", 18, "bold"),fg="#827972", background='#fbf8f3')
label.pack(side="top")

space = Label(text="", background='#fbf8f3')
space.pack(side="top")

replay_button = Button(text="Replay", font=("Courier New", 10), fg="#827972", bg="#ded5cc", command=lambda: window.destroy())
replay_button.grid(row=1, column=0, columnspan=2)

space = Label(text="", background='#fbf8f3')
space.pack(side="top")

canvas = Canvas(window, width=width, height=height, background="#b8aea2")
canvas.pack(side="bottom")

puzzle_root = PuzzleRoot("reachable1.txt")

img = []
for i in range(16):
    img.append(PhotoImage(file="src/assets/"+str(i+1)+".png"))


class PuzzleSquare:
    def __init__(self, canvas, x, y,image):
        self.canvas = canvas
        self.x = x #column
        self.y = y #row
        self.width = 100
        self.height = 100
        self.image = self.canvas.create_image(self.x+self.width/2, self.y+self.height/2, image=image)

    def move(self, direction):
        move_x = [0,1,0,-1]
        move_y = [-1,0,1,0]
        x_i = self.x
        y_i = self.y
        while self.x!=x_i+move_x[direction]*100 or self.y!=y_i+move_y[direction]*100:
            self.canvas.move(self.image, move_x[direction]*2, move_y[direction]*2)
            self.x += move_x[direction]*2
            self.y += move_y[direction]*2
            sleep(0.005)
            canvas.update()   

number = []
for i in range(16):
    number.append(PuzzleSquare(canvas, puzzle_root.number_to_rowcol(i+1)[1]*100, puzzle_root.number_to_rowcol(i+1)[0]*100, img[i]))

def move_16(move_index):
    # move_x = [0,1,0,-1]
    # move_y = [-1,0,1,0]
    # move_index:
    # 0 : up, 1 : right, 2 : down, 3 : left
    if move_index == 0: #up
        for i in range(16):
            if number[i].y==number[15].y-100 and number[i].x==number[15].x:
                number[i].move(2)
                number[15].move(0)
                break
    
    elif move_index == 1:
        for i in range(16):
            if number[i].x==number[15].x+100 and number[i].y==number[15].y:
                number[i].move(3)
                number[15].move(1)
                break

    elif move_index==2: # down
        for i in range(16):
            if number[i].y==number[15].y+100 and number[i].x==number[15].x:
                number[i].move(0)
                number[15].move(2)
                break
    
    elif move_index==3:
        for i in range(16):
            if number[i].x==number[15].x-100 and number[i].y==number[15].y:
                number[i].move(1)
                number[15].move(3)
                break

move_16(2)
move_16(1)
move_16(2)


window.mainloop()


