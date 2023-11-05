fn main() {
    let file = include_str!("../inputs/2.txt");
    let grid: Vec<Vec<i64>> = file
        .lines()
        .map(|l| {
            l.chars()
                .map(|c| c.to_digit(10).unwrap() as i64)
                .collect()
        })
        .collect();

    let width: usize = grid[0].len();
    let height: usize = grid.len();

    // transposed grid
    let tgrid: Vec<Vec<i64>> = (0..grid[0].len())
        .map(|col| grid.iter().map(|row| row[col]).collect())
        .collect();
    // println!("{:?}", tgrid);
    
    // [ PART 1 - Gamma / Epsilon ]
    let counts: Vec<usize> = tgrid
        .iter()
        .map(|row| row.iter().filter(|&&c| c==1).count())
        .collect();
    // println!("{:?}", counts);

    let gamma: i64 = counts
        .iter()
        .enumerate()
        .map(|(index, value)| ((value >= &(height / 2)) as i64) << (&width-index-1))
        .sum::<i64>();
    // println!("{}", gamma);

    let epsilon: i64 = counts
        .iter()
        .enumerate()
        .map(|(index, value)| ((value < &(height / 2)) as i64) << (&width-index-1))
        .sum::<i64>();
    // println!("{}", epsilon);

    println!("Part 1: {}", gamma * epsilon);

    // [ PART 2 - Oxygen / CO2]

    // -- compute oxygen
    let mut ogrid = grid.clone();
    let mut i: usize = 0;
    while ogrid.len() > 1 {
        //
        let ones = ogrid.iter().map(|row| row[i]).collect::<Vec<i64>>()
            .iter().filter(|&&c| c == 1).count();
        let zeroes = ogrid.iter().map(|row| row[i]).collect::<Vec<i64>>()
            .iter().filter(|&&c| c == 0).count();
        let bit = if ones >= zeroes { 1 } else { 0 };

        // println!("{} {} {}", ones, zeroes, bit);

        //
        ogrid = ogrid
            .into_iter()
            .filter(|n| n[i] == bit)
            .collect();

        i += 1;
    }
    let oxygen = &ogrid[0]
        .iter()
        .enumerate()
        .map(|(index, value)| value << (&width-index-1))
        .sum::<i64>();
    // println!("{:?}", oxygen);

    // --- compute CO2
    let mut cgrid = grid.clone();
    let mut j = 0;
    while cgrid.len() > 1 {
        let ones = cgrid.iter().map(|row| row[j]).collect::<Vec<i64>>()
            .iter().filter(|&&c| c == 1).count();
        let zeroes = cgrid.iter().map(|row| row[j]).collect::<Vec<i64>>()
            .iter().filter(|&&c| c == 0).count();
        let bit = if zeroes <= ones { 0 } else { 1 };

        cgrid = cgrid
            .into_iter()
            .filter(|n| n[j] == bit)
            .collect();

        j += 1;
    }
    let co2 = &cgrid[0]
        .iter()
        .enumerate()
        .map(|(index, value)| value << (&width-index-1))
        .sum::<i64>();

    // println!("{} {}", oxygen, co2);
    print!("Part 2: {}", oxygen * co2);

}
