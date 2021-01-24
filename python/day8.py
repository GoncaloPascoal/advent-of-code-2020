
import os

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    instructions = []

    for line in f:
        line = line.strip()
        
        opcode, arg = line.split()
        instructions.append((opcode, int(arg)))
    
    return instructions

# Complexity: O(n)
def find_loop(instructions):
    acc = 0
    pc = 0  # Program counter, or instruction pointer

    executed = set()

    while True:
        if pc in executed:
            return acc, False
        elif pc >= len(instructions):
            return acc, True
        
        executed.add(pc)
        opcode, arg = instructions[pc]

        if opcode == 'acc':
            acc += arg
            pc += 1
        elif opcode == 'jmp':
            pc += arg
        elif opcode == 'nop':
            pc += 1

# Complexity: O(n^2), could probably be improved
def fix_loop(instructions):
    for i in range(len(instructions)):
        opcode, arg = instructions[i]

        if opcode == 'jmp' or opcode == 'nop':
            modified = instructions.copy()
            modified_opcode = 'nop' if opcode == 'jmp' else 'jmp'
            modified[i] = (modified_opcode, arg)
            
            acc, halts = find_loop(modified)

            if halts:
                return acc

instructions = parse_file('../data/day8.txt')

# Part 1
print(find_loop(instructions)[0])

# Part 2
print(fix_loop(instructions))
