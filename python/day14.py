
import os

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    return [line.strip() for line in f]


def set_bit(value, bit, bit_value):
    if bit_value == 1:
        return value | (1 << bit)
    elif bit_value == 0:
        return value & ~(1 << bit)
    return value

def get_possible_combinations(num_floating):
    combinations = []

    for i in range(2 ** num_floating):
        combinations.append(list(bin(i)[2:].zfill(num_floating)))
    
    return combinations

# Complexity: scary if number of floating bits is high
def get_sum_memory(commands, version):
    memory = {}

    for command in commands:
        left, right = command.split(' = ')

        if left == 'mask':
            mask = right
        else:
            right = int(right)
            left = left[4:-1] # Remove mem[] wrapper (only the memory location is left)

            if version == 1:
                for bit, bit_value in enumerate(reversed(mask)):
                    if bit_value != 'X':
                        right = set_bit(right, bit, int(bit_value))
                
                memory[left] = right
            elif version == 2:
                left = bin(int(left))[2:].zfill(36)
                num_floating = 0

                for i, bit_value in enumerate(mask):
                    if bit_value != '0':
                        left = left[:i] + bit_value + left[i + 1:]
                        if bit_value == 'X': num_floating += 1
                
                combinations = get_possible_combinations(num_floating)

                for combination in combinations:
                    address = left[:]
                    combination_i = 0
                    
                    for i, bit in enumerate(address):
                        if bit == 'X':
                            address = address[:i] + combination[combination_i] + address[i + 1:]
                            combination_i += 1

                    memory[str(int(address, 2))] = right
    
    return sum(memory.values())


commands = parse_file('../data/day14.txt')

# Part 1
print(get_sum_memory(commands, 1))

# Part 2
print(get_sum_memory(commands, 2))