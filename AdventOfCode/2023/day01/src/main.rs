use std::collections::HashMap;

fn main() {
    // 1. read inputs
    let inputs: Vec<&str> = include_str!("../inputs/2.txt")
        .lines()
        .collect();
    // println!("{:?}", inputs);

    // [ PART 1 - Compute calibrations values ]
    let calibrations: Vec<i32> = inputs.iter().map(|word| {
        // get first and last digit
        let first_digit = word.chars().find(|c| c.is_digit(10)).unwrap();
        let last_digit = word.chars().rev().find(|c| c.is_digit(10)).unwrap();

        // concat first and last digit
        let calibration_value = format!("{}{}", first_digit, last_digit)
            .parse::<i32>()
            .expect("Failed to parse calibration value");
        calibration_value
    }).collect();
    // println!("{:?}", calibrations);

    println!("PART 1 - Calibration Value: {}", calibrations.iter().sum::<i32>());


    // [ PART 2 - Compute calibrations values with maps]

    // create dictionary of mapping
    let mut dictionary = HashMap::new();
    dictionary.insert("one", "1");
    dictionary.insert("two", "2");
    dictionary.insert("three", "3");
    dictionary.insert("four", "4");
    dictionary.insert("five", "5");
    dictionary.insert("six", "6");
    dictionary.insert("seven", "7");
    dictionary.insert("eight", "8");
    dictionary.insert("nine", "9");
    dictionary.insert("zero", "0");

}

