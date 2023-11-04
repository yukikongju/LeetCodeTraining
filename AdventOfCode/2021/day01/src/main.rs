#![feature(array_windows)]

// https://github.com/timvisee/advent-of-code-2021/blob/master/day01a/src/main.rs
fn main() {
    let file_contents = include_str!("../2.txt");
    let depths: Vec<u16> = file_contents
        .lines()
        .map(|n| n.parse().unwrap())
        .collect();

    // [ PART 1 ]
    let increases: usize = depths.array_windows::<2>()
        .filter(|[a,b]| a < b)
        .count();

    // println!("{:?}", depths);
    println!("PART 1: {}", increases);

    // [ PART 2 ]
    let measurements: Vec<u16> = depths
        .array_windows::<3>()
        .map(|[a,b,c]| a+b+c)
        .collect();
    let measurement_increases: usize = measurements
        .array_windows::<2>()
        .filter(|[a,b]| a < b)
        .count();

    // println!("{:?}", measurements);
    println!("PART 2: {}", measurement_increases);
}
