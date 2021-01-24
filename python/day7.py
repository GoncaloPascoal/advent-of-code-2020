
import os

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    return [line.strip() for line in f]

def parse_rules(lines):
    rules = {}

    for line in lines:
        line = line[:-1] # Remove dot at the end of the line
        before, after = line.split(' contain ')

        outer_parts = before.split()
        outer_bag = ' '.join(outer_parts[:2])

        inner_bags = {}

        if after != 'no other bags':
            for bag_str in after.split(', '):
                inner_parts = bag_str.split()
                inner_bag = ' '.join(inner_parts[1:3])
                inner_bags[inner_bag] = int(inner_parts[0])
        
        rules[outer_bag] = inner_bags

    return rules

# Complexity: don't know for sure, recursive solution
def get_outer_bag_colors(rules, bag_str):
    colors = set()

    for outer_bag in rules:
        if bag_str in rules[outer_bag]:
            colors.add(outer_bag)
            other_colors = get_outer_bag_colors(rules, outer_bag)
            colors = colors.union(other_colors)

    return colors

# Complexity: O(n), but not sure about this
def count_inner_bags(rules, bag_str):
    num_bags = 0

    for inner_bag, amount in rules[bag_str].items():
        num_bags += amount + amount * count_inner_bags(rules, inner_bag)

    return num_bags

lines = parse_file('../data/day7.txt')
rules = parse_rules(lines)

# Part 1
colors = get_outer_bag_colors(rules, 'shiny gold')
print(len(colors))

# Part 2
inner_bags = count_inner_bags(rules, 'shiny gold')
print(inner_bags)