
import os

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    grid = []

    for line in f:
        grid.append(line.strip())
    
    return grid

# Complexity: O(n)
def count_trees(grid, right, down):
    count = 0

    rows = len(grid)
    cols = len(grid[0])

    current_row = 0
    current_col = 0

    while current_row < rows:
        if (grid[current_row][current_col] == '#'):
            count += 1

        current_row += down
        current_col = (current_col + right) % cols

    return count

grid = parse_file('../data/day03.txt')
print(count_trees(grid, 3, 1))
print(count_trees(grid, 1, 1) * count_trees(grid, 3, 1) * count_trees(grid, 5, 1) * count_trees(grid, 7, 1) * count_trees(grid, 1, 2))