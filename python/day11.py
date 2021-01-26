
import os, copy

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    return [list(row.strip()) for row in f]

def count_adjacent_occupied_seats(grid, row, col, part):
    occupied = 0

    if part == 1:
        for i in range(max(row - 1, 0), min(row + 2, len(grid))):
            for j in range(max(col - 1, 0), min(col + 2, len(grid[i]))):
                if (i != row or j != col) and grid[i][j] == '#':
                    occupied += 1
    else:
        for row_inc in [-1, 0, 1]:
            for col_inc in [-1, 0, 1]:
                if row_inc != 0 or col_inc != 0:
                    current_row, current_col = row + row_inc, col + col_inc

                    while current_row >= 0 and current_row < len(grid) and current_col >= 0 and current_col < len(grid[0]):
                        if grid[current_row][current_col] != '.':
                            if grid[current_row][current_col] == '#':
                                occupied += 1
                            break
                        else:
                            current_row += row_inc
                            current_col += col_inc

    return occupied

def get_stable_state(grid, part):
    occupied_requirement = 4 if part == 1 else 5

    while True:
        new_grid = copy.deepcopy(grid)
        changed = False

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != '.':
                    occupied = count_adjacent_occupied_seats(grid, row, col, part)

                    if grid[row][col] == 'L' and occupied == 0:
                        new_grid[row][col] = '#'
                        changed = True
                    elif grid[row][col] == '#' and occupied >= occupied_requirement:
                        new_grid[row][col] = 'L'
                        changed = True

        if not changed:
            return new_grid
        else:
            grid = new_grid

def count_occupied_seats(grid):
    occupied = 0

    for row in grid:
        for elem in row:
            if elem == '#':
                occupied += 1
    
    return occupied

grid = parse_file('../data/day11.txt')

# Part 1
stable = get_stable_state(grid, 1)
print(count_occupied_seats(stable))

# Part 2
stable = get_stable_state(grid, 2)
print(count_occupied_seats(stable))