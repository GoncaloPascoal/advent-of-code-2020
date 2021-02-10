
puzzle_input = [20, 0, 1, 11, 6, 3]

# Complexity: O(n)
def get_nth_number_spoken(starting, n):
    if n <= len(starting):
        return starting[n - 1]
    
    last_pos = {}
    for i, number in enumerate(starting):
        last_pos[number] = i + 1

    while n > len(starting):
        previous = starting[-1]

        if previous not in last_pos:
            last_pos[previous] = len(starting)
            starting.append(0)
        else:
            starting.append(len(starting) - last_pos[previous])
            # Since we added an element, we have to subtract 1 to get the previous number's actual position
            last_pos[previous] = len(starting) - 1

    return starting[-1]

# Part 1
print(get_nth_number_spoken(puzzle_input, 2020))

# Part 2 (takes around 15 seconds to compute)
print(get_nth_number_spoken(puzzle_input, 30000000))