
import os

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    passwords = []

    for line in f:
        tokens = line.split(": ")
        policy = tokens[0].split()
        limits = policy[0].split("-")

        password = tokens[1]
        letter = policy[1]
        minimum = int(limits[0])
        maximum = int(limits[1])

        passwords.append((password, letter, minimum, maximum))
    
    return passwords

# Complexity: O(n^2) or O(n * m), depending on password size
def check_valid(passwords):
    count = 0

    for tup in passwords:
        password, letter, minimum, maximum = tup

        occurrences = password.count(letter)
        
        if occurrences >= minimum and occurrences <= maximum:
            count += 1

    return count

# Complexity: O(n)
def check_valid_new_policy(passwords):
    count = 0

    for tup in passwords:
        password, letter, first, second = tup

        # Using XOR (exactly one of the conditions must be true)
        if (password[first - 1] == letter) != (password[second - 1] == letter):
            count += 1
    
    return count

passwords = parse_file("../data/day2.txt")
print(check_valid(passwords))
print(check_valid_new_policy(passwords))
