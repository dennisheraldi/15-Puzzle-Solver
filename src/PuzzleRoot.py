from Puzzle import Puzzle

class PuzzleRoot(Puzzle):
    def __init__(self, filename):
        self.puzzle = []
        self.load_puzzle('../test/'+filename)
        self.kurang_i=[]
        self.value_X = 0
        self.move_index = -1
        self.difference = self.calc_difference()

    def load_puzzle(self, filename):
        with open(filename) as f:
            for line in f:
                self.puzzle.append(list(map(int, line.split())))
        self.pos_16 = self.find_ubin_position(16)
        self.row_16 , self.col_16 = self.pos_to_rowcol(self.pos_16)

    def calc_kurang_i(self):
        for i in range(16): # Untuk ubin bernomor i {1(0)..16(15)}
            count = 0
            pos_ubin_i = self.find_ubin_position(i+1)
            for j in range(pos_ubin_i+1,17): # POSISI(j) > POSISI(i)
                if (self.pos_to_number(j) < i+1): # j < i
                    count+=1
            self.kurang_i.append(count)

    def find_value_X(self):
        if ((self.row_16+self.col_16) % 2 == 1):
            self.value_X = 1

    def print_kurang_i(self):
        self.calc_kurang_i()
        for j in range(4):
            for i in range(4):
                print(f"Kurang({self.rowcol_to_pos(i,j)})={self.kurang_i[self.rowcol_to_pos(i,j)-1]}", end="\t")
            print()

    def print_kurang_i_plus_x(self):
        self.find_value_X()
        result = sum(self.kurang_i) + self.value_X
        print("Nilai dari Σ(i=1,16) Kurang(i) + X adalah", result)
    
    def is_puzzle_solvable(self):
        return (sum(self.kurang_i) + self.value_X)%2 == 0
