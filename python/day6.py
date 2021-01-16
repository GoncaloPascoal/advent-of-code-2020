
import os

# Complexity: O(n * m), n is number of people and m number of questions
def anyone(lines):
    groups = []
    group = set()

    for line in lines:
        if line:
            for letter in line:
                group.add(letter)
        else:
            groups.append(group)
            group = set()
    
    if group:
        groups.append(group)
    
    return groups

# Complexity: O(n * m), n is number of people and m number of questions
def everyone(lines):
    groups = []
    group = {}
    members = 0

    for line in lines:
        if line:
            for letter in line:
                if letter in group:
                    group[letter] += 1
                else:
                    group[letter] = 1
            members += 1
        else:
            to_delete = [letter for letter in group if group[letter] != members]
            for letter in to_delete:
                del group[letter]
            groups.append(group)
            group = {}
            members = 0
    
    if group:
        to_delete = [letter for letter in group if group[letter] != members]
        for letter in to_delete:
            del group[letter]
        groups.append(group)
    
    return groups

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    return [line.strip() for line in f]

lines = parse_file('../data/day6.txt')

groups_anyone = anyone(lines)
groups_everyone = everyone(lines)

print(sum(map(len, groups_anyone)))
print(sum(map(len, groups_everyone)))

