import math

def lattice_paths(width):
    
    paths = math.comb(width * 2, width)
    print(paths)
    
lattice_paths(20)