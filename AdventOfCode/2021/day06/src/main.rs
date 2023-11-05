fn main() {
    // -- 1. 
    let lanterns: Vec<i32> = include_str!("../inputs/2.txt")
        .lines()
        .flat_map(|l| l.split(",").map(|c| c.parse().unwrap()))
        .collect();
    // print!("{:?}", lanterns);

    // [ PART 1 - ]
    const NUM_DAYS: i32 = 80;
    let mut population = lanterns.clone();
    for day in 0..NUM_DAYS {
        let num_zeroes = population.iter().filter(|&p| *p==0).count();
        population = population.iter_mut().map(|p| if *p == 0 { 6 } else { *p-1 }).collect();
        for _ in 0..num_zeroes {
            population.push(8);
        }
        // println!("{:?}", population);
    }

    print!("[ Part 1 ] Population size: {}", population.len());


}
