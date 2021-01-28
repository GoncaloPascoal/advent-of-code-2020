
import os, math

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    instructions = []

    for instruction in f:
        instruction = instruction.strip()
        
        instructions.append((instruction[:1], int(instruction[1:])))
    
    return instructions

# Complexity: O(n)
def get_final_position(instructions):
    # Ship starts at origin, function returns resulting position after following instructions
    pos = [0, 0]
    angle = 0

    for action, value in instructions:
        if action == 'N':
            pos[1] += value
        elif action == 'S':
            pos[1] -= value
        elif action == 'E':
            pos[0] += value
        elif action == 'W':
            pos[0] -= value
        elif action == 'L':
            angle += value
        elif action == 'R':
            angle -= value
        elif action == 'F':
            angle_rad = math.radians(angle)

            pos[0] += math.cos(angle_rad) * value
            pos[1] += math.sin(angle_rad) * value

    return list(map(lambda x: round(x, 4), pos))


def rotate(vec, angle):
    return [
        math.cos(angle) * vec[0] - math.sin(angle) * vec[1],
        math.sin(angle) * vec[0] + math.cos(angle) * vec[1]
    ]

# Complexity: O(n)
def get_final_position_waypoint(instructions, waypoint):
    pos = [0, 0]

    for action, value in instructions:
        if action == 'N':
            waypoint[1] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'W':
            waypoint[0] -= value
        elif action == 'L':
            waypoint = rotate(waypoint, math.radians(value))
        elif action == 'R':
            waypoint = rotate(waypoint, math.radians(-value))
        elif action == 'F':
            pos[0] += waypoint[0] * value
            pos[1] += waypoint[1] * value
    
    return list(map(lambda x: round(x, 4), pos))


instructions = parse_file('../data/day12.txt')

# Part 1
final_pos = get_final_position(instructions)
print(abs(final_pos[0]) + abs(final_pos[1]))

# Part 2
final_pos = get_final_position_waypoint(instructions, [10, 1])
print(abs(final_pos[0]) + abs(final_pos[1]))