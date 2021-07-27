
use std::fs::File;
use std::io::Read;
use std::path::Path;

struct PasswordPolicy {
    char: char,
    min: usize,
    max: usize,
    password: String,
}

fn parse_file(path: &str) -> Vec<PasswordPolicy> {
    let path = Path::new(path);

    let mut file = match File::open(path) {
        Err(message) => panic!("Couldn't open file: {}", message),
        Ok(file) => file,
    };

    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(message) => panic!("Couldn't read file: {}", message),
        Ok(_) => (),
    }
    s = s.trim().to_string();

    let mut policies = vec![];

    for line in s.lines() {
        // Parse lines formatted as [min]-[max] [char]: [password]

        let mut parts = line.split(" ");

        let mut range_iter = parts.next().unwrap().split("-");
        let min = range_iter.next().unwrap().parse().unwrap();
        let max = range_iter.next().unwrap().parse().unwrap();

        let char = parts.next().unwrap().chars().next().unwrap();
        let password = parts.next().unwrap().to_string();

        let policy = PasswordPolicy {
            char,
            min,
            max,
            password,
        };

        policies.push(policy);
    }
    
    policies
}

fn num_valid_passwords(policies: &Vec<PasswordPolicy>) -> usize {
    let mut counter = 0;

    for policy in policies {
        let matches = policy.password.match_indices(policy.char).count();
        if matches >= policy.min && matches <= policy.max {
            counter += 1;
        }
    }

    counter
}

fn num_actual_valid_passwords(policies: &Vec<PasswordPolicy>) -> usize {
    let mut counter = 0;

    for policy in policies {
        let first = policy.password.chars().skip(policy.min - 1).next().unwrap();
        let second = policy.password.chars().skip(policy.max - 1).next().unwrap();

        if (first == policy.char) != (second == policy.char) {
            counter += 1;
        }
    }

    counter
}

pub fn print_results() {
    let policies = parse_file("../../data/day02.txt");

    println!("{} passwords are valid according to the policies.", num_valid_passwords(&policies));
    println!("{} passwords are valid according to the correct policies.", num_actual_valid_passwords(&policies));
}
