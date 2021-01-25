
import os

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    adapters = set()

    for l in f:
        adapters.add(int(l.strip()))
    
    return adapters

# Complexity: O(n)
def calculate_jolt_differences(adapters):
    jolts = 0

    # 3 jolt difference starts at 1 since built-in adapter is always 3 jolts higher than max adapter
    diffs = [0, 0, 1]

    max_adapter = max(adapters)

    while jolts != max_adapter:
        for i in range(1, 4):
            if jolts + i in adapters:
                jolts = jolts + i
                diffs[i - 1] += 1
                break
        else:
            print('Cannot continue adapter chain')
            return
    
    return diffs[0] * diffs[2]

# Complexity: O(n)
def calculate_num_arrangements(adapters):
    jolts = 0
    num_arrangements = 1

    built_in = max(adapters) + 3
    adapters.add(built_in)

    while jolts != built_in:
        # Calculate diffs of owned adapters for the current jolts
        diffs = []
        for diff in range(1, 4):
            if jolts + diff in adapters:
                diffs.append(diff)
        
        # Calculate total number of combinations of owned adapters
        combinations = 2 ** len(diffs)

        # Essentially, for each adapter, we check if sequences that end in it are valid. If not, we remove those sequences
        # from the number of possible combinations. If all adapters can be at the end of the sequence, we remove only the case
        # where none of them are present.
        for i in reversed(diffs):
            can_be_at_end = False

            for j in range(jolts + 4, jolts + i + 4):
                if j in adapters or j > built_in:
                    can_be_at_end = True
                    break
            
            if not can_be_at_end:
                combinations -= 2 ** i
                break
        else:
            combinations -= 1

        num_arrangements *= combinations

        jolts += max(diffs)

    return num_arrangements

adapters = parse_file('../data/day10.txt')

# Part 1
print(calculate_jolt_differences(adapters))

# Part 2
print(calculate_num_arrangements(adapters))
