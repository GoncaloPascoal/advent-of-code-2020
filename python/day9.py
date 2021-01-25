
import os

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    return [int(l) for l in f]

# Complexity: O(n * m), n is sequence length, m is prelude length
def find_invalid(numbers, prelude_length):
    i = 0
    previous = set()

    # Add numbers to prelude
    while i != prelude_length:
        previous.add(numbers[i])
        i += 1
    
    while i != len(numbers):
        number = numbers[i]
        
        valid = False

        for first in previous:
            second = number - first
            if second != first and second in previous:
                valid = True
                break
        
        if not valid:
            return number
        
        previous.remove(numbers[i - prelude_length])
        previous.add(number)
        i += 1

# Complexity: O(n)
def find_weakness(numbers, invalid):
    first_idx = 0
    last_idx = 2

    total = sum(numbers[first_idx:last_idx])

    # Range grows ahead if sum is smaller than target number, shrinks behind if sum is larger
    while total != invalid:
        if total > invalid:
            total -= numbers[first_idx]
            first_idx += 1
        else:
            total += numbers[last_idx]
            last_idx += 1
    
    return min(numbers[first_idx:last_idx]) + max(numbers[first_idx:last_idx])

numbers = parse_file('../data/day9.txt')

# Part 1
invalid = find_invalid(numbers, 25)
print(invalid)

# Part 2
print(find_weakness(numbers, invalid))