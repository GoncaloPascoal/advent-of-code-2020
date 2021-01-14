
import os, re

def parse_file(path):
    script_dir = os.path.dirname(__file__)
    f = open(os.path.join(script_dir, path), 'r')

    passports = []

    passport = {}

    for line in f:
        line = line.strip()
        if line:
            fields = line.split()
            for field in fields:
                key, value = field.split(":")
                passport[key] = value
        else:
            passports.append(passport)
            passport = {}
    
    if passport:
        passports.append(passport)
    
    return passports

# Complexity: O(n), assuming constant number of keys
def count_valid(passports):
    count = 0

    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for passport in passports:
        valid = True
        for key in required_keys:
            if key not in passport:
                valid = False
                break
        
        if valid:
            count += 1
    
    return count


def validate_height(str):
    if len(str) < 2:
        return False
    
    units = str[-2:]
    value = str[:-2]

    if not value.isdigit():
        return False

    value = int(value)

    if units == 'cm':
        return value >= 150 and value <= 193
    elif units == 'in':
        return value >= 59 and value <= 76
    
    return False

# Complexity: O(n), assuming constant number of keys
def count_valid_with_validation(passports):
    count = 0

    conditions = {
        'byr': lambda x: x.isdigit() and (int(x) >= 1920 and int(x) <= 2002), 
        'iyr': lambda x: x.isdigit() and (int(x) >= 2010 and int(x) <= 2020), 
        'eyr': lambda x: x.isdigit() and (int(x) >= 2020 and int(x) <= 2030), 
        'hgt': validate_height, 
        'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x), 
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'], 
        'pid': lambda x: x.isdigit() and len(x) == 9
    }

    for passport in passports:
        valid = True
        for key in conditions:
            if not(key in passport and conditions[key](passport[key])):
                valid = False
                break
        
        if valid:
            count += 1
    
    return count

passports = parse_file("../data/day4.txt")
print(count_valid(passports))
print(count_valid_with_validation(passports))