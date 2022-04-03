from Puzzle import Puzzle

class PuzzleRoot(Puzzle):
    def __init__(self, filename):
        self.puzzle = []
        self.load_puzzle(filename)
        self.kurang_i=[]
        self.value_X = 0
        self.move_index = -1
        self.difference = self.calc_difference()
        self.calc_kurang_i() # Menghitung nilai kurang_i
        self.find_value_X() # Mencari nilai X
        self.puzzle_info = ""
        self.puzzle_info_gui() # Mencetak informasi puzzle untuk gui
        self.print_puzzle_info_cli() # Mencetak informasi puzzle untuk CLI

    # Method untuk menerima input puzzle dari file
    def load_puzzle(self, filename):
        with open(filename) as f:
            for line in f:
                self.puzzle.append(list(map(int, line.split())))
        self.pos_16 = self.find_ubin_position(16)
        self.row_16 , self.col_16 = self.pos_to_rowcol(self.pos_16)
        print("\nPuzzle berhasil dimuat.")

    # Method untuk mencari nilai kurang i untuk setiap ubin
    def calc_kurang_i(self):
        for i in range(16): # Untuk ubin bernomor i {1(0)..16(15)}
            count = 0
            pos_ubin_i = self.find_ubin_position(i+1)
            for j in range(pos_ubin_i+1,17): # POSISI(j) > POSISI(i)
                if (self.pos_to_number(j) < i+1): # j < i
                    count+=1
            self.kurang_i.append(count)

    # Method untuk mencari nilai X
    def find_value_X(self):
        if ((self.row_16+self.col_16) % 2 == 1):
            self.value_X = 1

    # Method untuk mencetak kurang_i
    def print_kurang_i(self):
        print("\nNilai Kurang(i) untuk setiap ubin tersebut: \n")
        for j in range(4):
            for i in range(4):
                print(f"Kurang({self.rowcol_to_pos(i,j)})={self.kurang_i[self.rowcol_to_pos(i,j)-1]}", end="\t")
            print()  

    # Method untuk mencetak sum of kurang_i + value X
    def print_kurang_i_plus_x(self):
        result = sum(self.kurang_i) + self.value_X
        print("\nNilai dari Σ(i=1,16) Kurang(i) + X adalah", result)
    
    # Method untung mengecek apakah puzzle dapat diselesaikan atau tidak 
    # berdasarkan nilai sum of kurang_i + value X
    def is_puzzle_solvable(self):
        return (sum(self.kurang_i) + self.value_X)%2 == 0

    # Method untuk mencetak informasi puzzle di CLI
    def print_puzzle_info_cli(self):
        self.print_puzzle()
        self.print_kurang_i()
        self.print_kurang_i_plus_x()

    # Method untuk GUI
    def puzzle_info_gui(self):
        self.puzzle_info+="\nNilai Kurang(i) untuk setiap ubin tersebut: \n"
        for i in range(8):
            self.puzzle_info+="Kurang("+str(i+1)+") = "+str(self.kurang_i[i])+"\t\t"
            self.puzzle_info+="Kurang("+str(i+9)+") = "+str(self.kurang_i[i+8])+"\n"


        self.puzzle_info+= f"\nNilai dari Σ(i=1,16) Kurang(i) + X adalah {sum(self.kurang_i) + self.value_X}\n"
        if self.is_puzzle_solvable():
            self.puzzle_info+= "\nPuzzle dapat diselesaikan. \n\n"
        else:
            self.puzzle_info+= "\nPuzzle tidak dapat diselesaikan. \n\n"
