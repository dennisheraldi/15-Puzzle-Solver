from cgitb import text
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from time import *
from PuzzleRoot import PuzzleRoot
from Solver import SolvePuzzle

# Inisialisasi GUI
class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("15 Puzzle Solver")
        self.window.resizable(width=False, height=False)
        self.window.configure(background='#fbf8f3')

        self.img = []
        for i in range(16):
            self.img.append(PhotoImage(file="src/assets/"+str(i+1)+".png"))

        self.label_title = Label(text="15-Puzzle Solver", font=("Courier New", 18, "bold"),fg="#827972", background='#fbf8f3')
        self.label_title.pack(ipadx=10, ipady=10, fill='x',side="top")

        self.filename = ""
        self.load_file_button = Button(
            text="Load Puzzle", 
            command=lambda: self.load_file(), 
            font=("Courier New", 10, "bold"), 
            fg="#827972", 
            background='#fbf8f3'
            )    
        self.load_file_button.pack(
            ipadx=5, ipady=5
        )

        self.solve_button_clicked = False
        self.solve_button = Button(
            text="Solve Puzzle",
            command=lambda: self.solve_puzzle(),
            font=("Courier New", 10, "bold"),
            fg="#827972",
            background='#fbf8f3',
            state="disabled"
        )
        self.solve_button.pack(
            ipadx=5, ipady=5
        )
        self.solve_button_reload()

        self.label_dir = Label(text="Selected path:\n", font=("Courier New", 9, "bold"), fg="#827972", background='#fbf8f3')
        self.label_dir.pack(ipadx=10, ipady=10, fill='x',side="top")
        self.label_dir_reload()

        self.number=[]
        self.canvas = Canvas(self.window, width=400, height=400, background="#b8aea2")
        self.canvas.pack(side="left")
    
        self.scrollbar = Scrollbar(self.window)
        self.text_result = Text(self.window, width=50, height = 25, font=("Courier New", 9, "bold"), fg="#827972", background='#fbf8f3')
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text_result.pack(side = "right")
        self.scrollbar.config(command=self.text_result.yview)
        self.text_result.config(yscrollcommand=self.scrollbar.set)
        self.text_result.insert(END,"Result:\n\n")
        self.is_info_printed = False


    def load_file(self):
        self.solve_button_clicked = False
        self.text_result.delete("1.0",END)
        
        filetypes = (
            ("Text Files", "*.txt"),
        )
        
        self.filename = fd.askopenfilename(
            title = 'Select puzzle file',
            initialdir='test/',
            filetypes = filetypes)

        self.puzzle_root = PuzzleRoot(self.filename)
        
        self.text_result.insert(END,"Result: \n\n" +self.puzzle_root.puzzle_info)

        self.canvas.delete("all")
        for i in range(16):
                self.number.append(
                    PuzzleSquare(self.canvas, 
                    self.puzzle_root.number_to_rowcol(i+1)[1]*100, 
                    self.puzzle_root.number_to_rowcol(i+1)[0]*100, 
                    self.img[i]))

        showinfo(
            title = 'File Selected',
            message = 'You selected: ' + self.filename
        )

        if self.puzzle_root.is_puzzle_solvable():
            showinfo(title = 'Solvable Puzzle', message = 'Puzzle is solvable')
        else:
            showinfo(title = 'Unsolvable Puzzle', message = 'Puzzle is unsolvable')
        
    def label_dir_reload(self):
        self.label_dir.configure(text="Selected path:\n" + self.filename)
        self.label_dir.after(400, self.label_dir_reload)

    def solve_button_reload(self):
        if self.filename != "":
            if self.puzzle_root.is_puzzle_solvable():
                self.solve_button.configure(state="normal")
            else:
                self.solve_button.configure(state="disabled")
        self.solve_button.after(400, self.solve_button_reload)

    def move_16(self,move_index):
        move_x = [0,1,0,-1]
        move_y = [-1,0,1,0]
        moving = [2,3,0,1]
        # move_index:
        # 0 :#  up, 1 : right, 2 : down, 3 : left
        for i in range(16):
            if (self.number[i].y == self.number[15].y+100*move_y[move_index] and self.number[i].x == self.number[15].x+100*move_x[move_index]):
                self.number[i].move(moving[move_index])
                self.number[15].move(move_index)
                break

    def solve_puzzle(self):
        self.solve_button_clicked = True
        self.text_result.insert(END, "Pencarian solusi dilakukan...\n")
        self.solved = SolvePuzzle(self.puzzle_root)
        self.text_result.insert(END, f"Waktu eksekusi pencarian: {self.solved.exc_time:.6f} s\n")
        self.text_result.insert(END, f"Jumlah simpul yang dibangkitkan: {self.solved.generated_node} \n")
        self.text_result.insert(END, "\nLangkah penyelesaian: \n")
        for i in range(len(self.solved.steps)):
            langkah = ["UP","RIGHT","DOWN","LEFT"]
            self.text_result.insert(END,"Langkah ke-"+str(i+1)+": "+langkah[self.solved.steps[i]]+"\n")
            self.move_16(self.solved.steps[i])
        self.text_result.insert(END, "\nPuzzle berhasil diselesaikan!\n")
        
        
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
            self.canvas.move(self.image, move_x[direction]*4, move_y[direction]*4)
            self.x += move_x[direction]*4
            self.y += move_y[direction]*4
            sleep(0.005)
            self.canvas.update()

gui = GUI(Tk())
gui.window.mainloop()


