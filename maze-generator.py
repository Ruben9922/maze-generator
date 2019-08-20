import numpy as np
import matplotlib.pyplot as plt
import vectormath as vmath


def input_int(prompt, default=None, min=None, max=None):
    input_valid = False
    while not input_valid:
        s = input(f"{prompt} (leave blank for {default}): ")
        try:
            x = int(s)
            if (min is None or x >= min) and (max is None or x <= max):
                input_valid = True
                return x
            else:
                if min is not None and max is not None:
                    print(f"Integers between {min} and {max} (inclusive) only!")
                elif min is not None:
                    print(f"Integers greater than or equal to {min} only!")
                else:
                    print(f"Integer less than or equal to {max} only!")
        except ValueError as e:
            if default is not None and s == "":
                return default
            else:
                print("Integers only!")


def compute_frontier_cells(cell):
    neighbours = {(cell[0] - 1, cell[1]), (cell[0], cell[1] - 1), (cell[0] + 1, cell[1]), (cell[0], cell[1] + 1)}

    # Removing walls that are out-of-bounds and walls
    neighbours = set(neighbour for neighbour in neighbours if
                     0 <= neighbour[0] < height and 0 <= neighbour[1] < width and grid[neighbour] == 1)

    return neighbours


def compute_neighbours(cell):
    neighbours = {(cell[0] - 1, cell[1]), (cell[0], cell[1] - 1), (cell[0] + 1, cell[1]), (cell[0], cell[1] + 1)}

    # Removing walls that are out-of-bounds and walls
    neighbours = set(neighbour for neighbour in neighbours if
                     0 <= neighbour[0] < height and 0 <= neighbour[1] < width and grid[neighbour] == 0)

    return neighbours


width = input_int("Width", 20, 0, None)
height = input_int("Height", width, 0, None)

# Create grid full of walls
# 1 represents wall; 0 represents non-wall
grid = np.ones((height, width))

# Pick cell and mark as non-wall
initial_cell = (np.random.randint(height), np.random.randint(width))
grid[initial_cell] = 0

# Create wall set
frontier_set = set()

# Get neighbouring walls and add to wall set
neighbouring_walls = compute_frontier_cells(initial_cell)
frontier_set.update(neighbouring_walls)

while len(frontier_set) != 0:
    print(f"wall set: {frontier_set}")
    # Pick arbitrary wall from wall set and remove
    frontier_cell = frontier_set.pop()

    print(f"wall:{frontier_cell}")
    print(compute_neighbours(frontier_cell))

    # If only one of the neighbouring cells is a non-wall, then change the wall to a non-wall and add neighbouring walls
    # to wall list
    if len(compute_neighbours(frontier_cell)) == 1:
        grid[frontier_cell] = 0
        neighbouring_walls = compute_frontier_cells(frontier_cell)
        frontier_set.update(neighbouring_walls)

plt.imshow(grid, cmap="gray_r", vmin=0, vmax=1)
plt.show()
