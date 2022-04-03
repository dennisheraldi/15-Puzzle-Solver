from PuzzleRoot import PuzzleRoot
from Solver import SolvePuzzle

if __name__ == "__main__":
    print("\n15-Puzzle Solver")
    print("---------------------------")
    filename = input("\nMasukkan nama file puzzle yang akan diselesaikan (.txt): ")
    filename = "test/" + filename

    puzzle_root = PuzzleRoot(filename)

    if not puzzle_root.is_puzzle_solvable():
        print("\nPuzzle tidak dapat diselesaikan.\n")
    else:
        print("\nPuzzle dapat diselesaikan. \n")
        solve = SolvePuzzle(puzzle_root)
        
        
        

    

