use std::collections::HashMap;

const BINGO_SIZE: usize = 5;


fn main() {
    // -- 1. reading the inputs
    let lines: Vec<&str> = include_str!("../inputs/1.txt").lines().collect();
    let numbers: Vec<i32> = lines[0]
        .split(',')
        .map(|num_str| num_str.parse().unwrap())
        .collect();
    // print!("{:?}", numbers);

    let mut bingos: Vec<Vec<Vec<i32>>> = Vec::new();
    let mut bingo: Vec<Vec<i32>> = Vec::new();
    for (i, line) in lines[1..].iter().enumerate() {
        if i % 6 != 0 {
            let row: Vec<i32> = line
                .split_whitespace()
                .map(|num_str| num_str.parse().unwrap())
                .collect();
            bingo.push(row);
        } else {
            bingos.push(bingo);
            bingo = Vec::new();
        }
    }
    bingos.push(bingo);
    bingos = bingos[1..].to_vec();

    print!("{:?}", bingos);

    // [ Part 1 - BINGO ]

    // precompute: for each bingo, store position of value in dict => {num : (bingo, x, y)}
    let mut positions: HashMap<i32, Vec<(usize, usize, usize)>> = HashMap::new(); 
    for number in numbers.iter() {
        positions.insert(*number, Vec::new());
    }

    for (i, bingo) in bingos.iter().enumerate() {
        let flattened: Vec<(usize, usize, i32)> = bingo
            .iter()
            .enumerate()
            .flat_map(|(row_index, row)| {
                row.iter().enumerate().map(move |(col_index, &value)| (row_index, col_index, value))
            }).collect();

        for (row, col, value) in flattened {
            positions.get_mut(&value).unwrap().push((i, row, col));
        }
    }

    // run bingo: for each number: (1) set each bingo number (2) check if we have a bingo
    let mut founds: Vec<Vec<Vec<bool>>> = Vec::new();
    founds = (0..bingos.len()) 
        .map(|_| {
            (0..BINGO_SIZE).map(|_| vec![false; BINGO_SIZE]).collect()
        }).collect();
    for (i, num) in numbers.iter().enumerate() {
        // put drawn number in each bingo
        for (idx_bingo, x, y) in positions.get(num).unwrap() {
            founds[*idx_bingo][*x][*y] = true; 
        }

        // check if we have a bingo: vertical and horizontal
        // founds
        //     .iter()
        //     .map(|found| {
        //         let vert = std::all_true(found.begin(), found.end())

        //     })
    }

    // compute bingo score

    // [ Part 2 - ]


}
