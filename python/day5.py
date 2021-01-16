
import os

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    return [line.strip() for line in f]

def get_seat_id(str):
    row = str[:7]
    col = str[7:]

    # To get the row and column we can simply convert the strings to binary
    row = int(row.replace('F', '0').replace('B', '1'), 2)
    col = int(col.replace('L', '0').replace('R', '1'), 2)

    return row * 8 + col

# Complexity: O(n), where n is the number of seats
def find_seat(seat_ids):
    for i in range(128 * 8):
        if i not in seat_ids and i - 1 in seat_ids and i + 1 in seat_ids:
            return i
    
    return None

lines = parse_file('../data/day5.txt')
seat_ids = set(map(get_seat_id, lines))
print(max(seat_ids))
print(find_seat(seat_ids))