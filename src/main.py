from bnb import *

mat = Puzzle()
mat.load_puzzle('../test/reachable1.txt')
mat.print_puzzle()
mat.move_left()
print(mat.calc_compare())


# for i in range(16):
#     print(f"ubin {i+1} ada di {mat.find_ubin_position(i+1)}")

