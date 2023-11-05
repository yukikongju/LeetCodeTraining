fn main() {
    let file = include_str!("../inputs/2.txt");
    let grid: Vec<Vec<u64>> = file
        .lines()
        .map(|l| {
            l.chars()
                .map(|c| c.to_digit(10).unwrap() as u64)
                .collect()
        })
        .collect();

    let width: usize = grid[0].len();
    let height: usize = grid.len();

    // transposed grid
    let tgrid: Vec<Vec<u64>> = (0..grid[0].len())
        .map(|col| grid.iter().map(|row| row[col]).collect())
        .collect();
    // println!("{:?}", tgrid);
    
    // [ PART 1 ]
    let counts: Vec<usize> = tgrid
        .iter()
        .map(|row| row.iter().filter(|&&c| c==1).count())
        .collect();
    // println!("{:?}", counts);

    let gamma: u64 = counts
        .iter()
        .enumerate()
        .map(|(index, value)| ((value >= &(height / 2)) as u64) << (&width-index-1))
        .sum::<u64>();
    // println!("{}", gamma);

    let epsilon: u64 = counts
        .iter()
        .enumerate()
        .map(|(index, value)| ((value < &(height / 2)) as u64) << (&width-index-1))
        .sum::<u64>();
    // println!("{}", epsilon);

    println!("Part 1: {}", gamma * epsilon);

    // [ PART 2 ]


}
