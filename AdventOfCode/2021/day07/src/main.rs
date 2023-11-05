fn main() {
    let positions: Vec<i32> = include_str!("../inputs/2.txt")
        .lines()
        .flat_map(|l| l.split(',').map(|c| c.parse().unwrap()))
        .collect();
    // println!("{:?}", positions);

    // [ Part 1 ]
    let min = *positions.iter().min().unwrap_or(&0);
    let max = *positions.iter().max().unwrap_or(&0);
    let diffs: Vec<i32> = (min..max)
        .map(|mid| positions.iter().map(|&p| (p-mid).abs()).sum::<i32>())
        .collect();
    // println!("{:?}", diffs);

    let min_fuel = &diffs.iter().min().unwrap_or(&0);
    println!("[PART 1] Min fuel: {}", min_fuel);

    // [ Part 2 - more expensive distance] sum n = n(n-1)/2
    let diffs2: Vec<i32> = (min..max)
        .map(|mid| positions.iter().map(|p| {
            let n = (p-mid).abs()+1;
            n * (n-1)/2
        }).sum::<i32>()).collect();

    let min_fuel2 = &diffs2.iter().min().unwrap_or(&0);
    println!("[PART 2] Min fuel: {}", min_fuel2);
}
