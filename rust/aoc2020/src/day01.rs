
// Required for reading from files
use std::fs::File;
use std::path::Path;
use std::io::prelude::*;

use std::collections::HashSet;

fn parse_file(path: &str) -> HashSet<i32> {
    let path = Path::new(path);

    let mut file = match File::open(&path) {
        Err(message) => panic!("Couldn't open file: {}", message),
        Ok(file) => file,
    };
    
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(message) => panic!("Couldn't read file: {}", message),
        Ok(_) => (),
    };
    s = s.trim().to_string();

    // Will panic if type conversion fails
    s.split('\n').map(|line| line.parse().unwrap()).collect()
}

fn find_pair(set: &HashSet<i32>, goal: i32) -> Option<(i32, i32)> {
    for first in set {
        let second = goal - first;

        if set.contains(&second) {
            return Some((*first, second));
        }
    }

    None
}

fn find_triplet(set: &HashSet<i32>) -> Option<(i32, i32, i32)> {
    for first in set {
        let goal = 2020 - first;
        
        if let Some((second, third)) = find_pair(set, goal) {
            return Some((*first, second, third));
        }
    }

    None
}

pub fn print_results() {
    let set = parse_file("../../data/day01.txt");

    let result = find_pair(&set, 2020);
    match result {
        Some(pair) => println!("Pair: {:?}\nProduct: {}\n", pair, pair.0 * pair.1),
        None => println!("Couldn't find pair"),
    }

    let result = find_triplet(&set);
    match result {
        Some(triplet) => println!("Triplet: {:?}\nProduct: {}", triplet, triplet.0 * triplet.1 * triplet.2),
        None => println!("Couldn't find triplet"),
    }
}
