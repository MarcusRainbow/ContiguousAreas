import numpy as np

def count_contiguous_areas(u):
    shape = np.shape(u)

    counter = 0

    # for each block of four pixels
    for x in range(0, shape[0] - 1):
        for y in range(0, shape[1] - 1):

            # convert the block to binary
            block = u[x, y] + 2 * u[x+1, y] + 4 * u[x, y+1] + 8 * u[x+1, y+1]

            # just two cases -- top left set, and bottom right unset
            if block == 1:
                counter += 1
            elif block == 7:
                counter -= 1

    return counter

def test_universe(universe, expected_areas):
        
    print(f"{universe}")

    areas = count_contiguous_areas(universe)
    
    print(f"number of contiguous areas: {areas}")
    assert(areas == expected_areas)

def test_square_block():
    universe = np.array([
        [0, 0, 0, 0],
        [0, 1, 1, 0], 
        [0, 1, 1, 0], 
        [0, 0, 0, 0]])
    test_universe(universe, 1)

def test_two_square_blocks():
    universe = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0], 
        [0, 1, 1, 0, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0]])
    test_universe(universe, 2)

def test_fancy_block():
    universe = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0], 
        [0, 1, 1, 1, 1, 1, 0], 
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]])
    test_universe(universe, 1)

def test_interleaved():
    universe = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], 
        [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
    test_universe(universe, 4)

if __name__ == '__main__':
    test_square_block()
    test_two_square_blocks()
    test_fancy_block()
    test_interleaved()
