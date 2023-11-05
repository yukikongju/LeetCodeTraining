fn main() {
    // -- 1. 
    let lanterns: Vec<usize> = include_str!("../inputs/2.txt")
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

    println!("[ Part 1 ] Population size: {}", population.len());

    // [ PART 2 - Using Map and array rotation]
    let mut map = lanterns.clone()
        .iter()
        .fold([0; 9], |mut map, &n| {
            map[n] += 1;
            map
        });

    (1..256).for_each(|day| map[(day + 7) % 9] += map[day % 9]);
    let pop_size: usize = map.iter().sum::<usize>();
    println!("[ Part 2 ] Population size: {}", pop_size);

}
