fn main() {
    let grid: Vec<Vec<i32>> = include_str!("../inputs/2.txt")
        .lines()
        .map(|l| {
            l.chars()
             .map(|c| c.to_digit(10).unwrap() as i32)
             .collect()
        }).collect();
    // println!("{:?}", grid);

    // [ PART 1 ]
    // let width: usize = grid[0].len();
    // let height: usize = grid.len();
    // let is_low: Vec<Vec<bool>> = grid
    //     .iter()
    //     .enumerate()
    //     .map(|(i, row)| {
    //         row.iter().enumerate().map(|(j, &c)| {
    //             let up = if (i as i32 -1)>=0 {c < grid[i-1][j]} else { true };
    //             let down = if i+1 < height { c < grid[i+1][j] } else { true };
    //             let left = if (j as i32 -1)>=0 { c < grid[i][j-1] } else { true };
    //             let right = if j+1 < width { c < grid[i][j+1] } else { true };
    //             up && down && left && right
    //         }).collect::<Vec<bool>>()
    //     }).collect();
    // println!("{:?}", is_low);

    let neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)];
    let mut low_points: Vec<i32> = Vec::new();
    for (i, line) in grid.iter().enumerate() {
        for (j, cell) in line.iter().enumerate() {
            if neighbors.iter().all(|&(dx, dy)| {
                grid.get((i as isize + dx) as usize)
                    .and_then(|l| l.get((j as isize + dy) as usize))
                    .map(|n| cell < n)
                    .unwrap_or(true)
            }) {
                low_points.push(*cell);
            }
        }
    }
    // println!("{:?}", low_points);
    let sum: i32 = low_points.iter().map(|p| p+1).sum();
    println!("[Part 1] Low Points Sum: {}", sum);

}
