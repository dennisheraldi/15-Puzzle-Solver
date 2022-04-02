from queue import PriorityQueue
from copy import deepcopy
from Puzzle import Puzzle

class Node:
    def __init__(self, parent, puzzle_obj, level):
        self.parent = deepcopy(parent) # parent node
        self.puzzle_obj = deepcopy(puzzle_obj)
        self.level = level
        self.cost = self.puzzle_obj.difference + self.level
    
    def __lt__(self, other):
        return self.cost < other.cost
         

class SolvePuzzle:
    # initial_puzzle telah terdefinisi sebagai objek puzzle state awal
    def __init__(self,initial_puzzle):
        # Counter simpul yang dibangkitkan
        self.generated_node = 0
        # Inisialisasi flag
        self.is_found = False
        # Inisialisasi steps untuk menyimpan langkah penyelesaian
        self.steps = [] 
        # Inisialisasi priority queue pada simpul hidup
        live_node = PriorityQueue()
        # Inisialisasi akar yaitu state awal puzzle 
        # parent = None, puzzle = initial_puzzle, level = 0
        root = Node(None, initial_puzzle, 0)
        self.generated_node+=1 # Akar dibangkitkan
        # Enqueue akar
        live_node.put(root)

        while (not (live_node.empty()) and not self.is_found):

            e_node = live_node.get()

            if (e_node.puzzle_obj.difference == 0): # Solusi ditemukan ketika semua ubin berada pada posisi sesuai nomor (difference = 0)
                self.print_solution(e_node)
                self.is_found = True
                print("\nJumlah simpul yang dibangkitkan:", self.generated_node)
                
            else:
                for i in range(4):
                    if ( (e_node.puzzle_obj.move_index%2 != i%2) or (e_node.puzzle_obj.move_index == i) or (e_node.parent == None) ): #
                        moved_puzzle = Puzzle(e_node.puzzle_obj.puzzle, i)
                        if moved_puzzle.move_index!=-1: #perpindahan valid maka tambahkan simpul
                            child = Node(e_node, moved_puzzle, e_node.level+1)
                            self.generated_node+=1
                            live_node.put(child)


    def print_solution(self, node):
        if(node.parent is None):
            print("Langkah penyelesaian:")
        else:
            self.print_solution(node.parent)
            print()
            # move_index:
            # 0 : up, 1 : right, 2 : down, 3 : left
            direction = ["UP", "RIGHT", "DOWN", "LEFT"]
            if node.puzzle_obj.move_index!=-1:
                self.steps.append(node.puzzle_obj.move_index)
                print(f"Langkah {len(self.steps)}: {direction[node.puzzle_obj.move_index]}")
                node.puzzle_obj.print_puzzle()



