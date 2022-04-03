from copy import deepcopy

class Puzzle:
    # Konstruktor untuk kelas Puzzle
    # Default = puzzle : array of array of int kosong []
    # Default = move_index : -1 (perpindahan belum dilakukan atau tidak valid) 
    def __init__(self, puzzle=[], move_index=-1):
        self.puzzle = deepcopy(puzzle)
        self.pos_16 = self.find_ubin_position(16)
        self.row_16, self.col_16 = self.pos_to_rowcol(self.pos_16)
        self.move_index = self.move(move_index)
        self.difference = self.calc_difference()

    # Method untuk mencetak status puzzle
    def print_puzzle(self): 
        for i in range(16):
            if (i==0):
                print(" _______________________")
            if (i in [1,4,7,10]):
                print("|     |     |     |     |")
            if (i in [2,5,8,11]):
                print("|",end="")
                for j in range(4):
                    print("  ",end="")
                    print((self.puzzle[(i-2)//3][j],"  ")[self.puzzle[(i-2)//3][j]==16],end="")
                    print(("  "," ")[self.puzzle[(i-2)//3][j]>9],end="|")
                print("")
            if (i in [3,6,9,12]):
                print("|_____|_____|_____|_____|")

    # Method untuk mencari posisi ubin 
    # Return: posisi ubin dalam puzzle {1..16}
    def find_ubin_position(self, number):
        i = 0
        found = False
        while (not found and i < 4):
            j = 0
            while(not found and j < 4):
                if self.puzzle[i][j] == number:
                    found = True
                j += 1 
            i += 1    
        return self.rowcol_to_pos(i-1,j-1)
    
    # Method untuk mengkonversi posisi row dan col ke posisi puzzle
    # Return: posisi dalam puzzle {1..16}
    def rowcol_to_pos(self,row,col):
        return (row*4)+col+1

    # Method untuk mengkonversi posisi puzzle ke posisi row dan col
    # Return: row {0..3} dan col {0..3}
    def pos_to_rowcol(self,pos):
        row = pos//4 if pos%4!=0 else pos//4-1
        col = pos%4-1 if pos%4!=0 else pos%4+3
        return row,col

    # Method untuk mengembalikan nilai angka ubin sesuai dengan masukan posisinya
    # Return: angka ubin {1..16}
    def pos_to_number(self, pos):
        row, col = self.pos_to_rowcol(pos)
        return self.puzzle[row][col]

    # Method untuk mencari row dan col dari suatu angka ubin
    # Return: row {0..3} dan col {0..3}
    def number_to_rowcol(self,number):
        for i in range(4):
            for j in range(4):
                if self.puzzle[i][j] == number:
                    return i,j
    
    # Method untuk menggerakkan ubin bernomor 16 sesuai dengan arahnya
    # Return: move_index {-1..3} <- mengindikasikan arah perpindahan
    def move(self, move_index):
        # move_index:
        # 0 : up, 1 : right, 2 : down, 3 : left
        row_move = [-1,0,1,0] 
        col_move = [0,1,0,-1]
        is_moving = False

        if move_index!= -1: # move indexnya valid
            moving_row = self.row_16 + row_move[move_index]
            moving_col = self.col_16 + col_move[move_index]

            if (moving_row >= 0 and moving_row < 4 
                and moving_col >=0 and moving_col < 4): # ubin setelah move valid
                is_moving = True
                swap = self.puzzle[moving_row][moving_col] # proses swapping
                self.puzzle[self.row_16][self.col_16]= swap
                self.puzzle[moving_row][moving_col] = 16
                self.row_16 = moving_row
                self.col_16 = moving_col
        
        if not is_moving: # if not move
            move_index = -1

        return move_index

    # method untuk menghitung perbedaan antara status puzzle saat ini dengan kondisi akhir
    # return : nilai perbedaan antara status puzzle saat ini dan kondisi akhir
    def calc_difference(self):
        count = 0
        for i in range(15):
            if (self.pos_to_number(i+1) != i+1):
                count+=1
        return count
