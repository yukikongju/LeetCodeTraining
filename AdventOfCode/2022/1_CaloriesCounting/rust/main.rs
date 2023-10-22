use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::io::Read;

fn main() {
    // open the file
    let file_path = "calories.txt";
    let mut file = match File::open(file_path) {
        Ok(file) => file,
        Err(e) => panic!("Failed to open file {}", e),
    };

    // read file line by line
    let mut elves: Vec<i32> = Vec::new();
    let reader = BufReader::new(file);
    for line in reader.lines() {
        match line {
            Ok(line) => {
                // process line
            }
            Err(e) => {
                panic!("Failed to read line: {}", e),
            }
        }
    }


    // 
    println!("{}", calories);
}
