from ctypes.util import find_msvcrt
from queue import PriorityQueue
import time

class Puzzle:
    def __init__(self):
        self.puzzle = []
        self.row = 4
        self.col = 4
        self.kurang_i=[]
        self.value_X = 0

    def load_puzzle(self, filename):
        with open(filename) as f:
            for line in f:
                self.puzzle.append(list(map(int, line.split())))

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

    def find_value_X(self):
        position_x = self.find_ubin_position(16)
        if position_x in [2,4,5,7,10,12,13,15]: # row+col%2 == 1
            self.value_X = 1
            
    def rowcol_to_pos(self,row,col):
        return (row*4)+col+1

    def pos_to_rowcol(self,pos):
        row = pos//4 if pos%4!=0 else pos//4-1
        col = pos%4-1 if pos%4!=0 else pos%4+3
        return row,col

    def pos_to_number(self, pos):
        row, col = self.pos_to_rowcol(pos)
        return self.puzzle[row][col]

    def calc_kurang_i(self):
        for i in range(16): # Untuk ubin bernomor i {1(0)..16(15)}
            count = 0
            pos_ubin_i = self.find_ubin_position(i+1)
            for j in range(pos_ubin_i+1,17): # POSISI(j) > POSISI(i)
                if (self.pos_to_number(j) < i+1): # j < i
                    count+=1
            self.kurang_i.append(count)
            
    def print_kurang_i(self):
        self.calc_kurang_i()
        for i in range(16):
            print(f"KURANG({i+1})={self.kurang_i[i]}")

    def print_kurang_i_plus_x(self):
        self.calc_kurang_i()
        self.find_value_X()
        sum_of_kurang_i = sum(self.kurang_i)
        result = sum_of_kurang_i + self.value_X
        print("Nilai dari Σ(i=1,16) KURANG(i) + X adalah", result)
    


    
