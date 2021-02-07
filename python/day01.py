
import os

def get_set_from_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    numbers = set()

    for line in f:
        numbers.add(int(line))
    
    return numbers

# Complexity: O(n)
def find_pair(numbers, goal):
    for first in numbers:
        second = goal - first

        if second in numbers:
            return first, second

# Complexity: O(n^2)
def find_triplet(numbers):
    for first in numbers:
        sum_other_two = 2020 - first
        result = find_pair(numbers, sum_other_two)

        if result:
            second, third = result
            return first, second, third


numbers = get_set_from_file("../data/day01.txt")
result = find_pair(numbers, 2020)

if result:
    first, other = result
    print("Found pair:", first, "x", other, "=", first * other)
else:
    print("Couldn't find pair")

result = find_triplet(numbers)

if result:
    first, second, third = result
    print("Found triplet:", first, "x", second, "x", third, "=", first * second * third)
else:
    print("Couldn't find pair")
