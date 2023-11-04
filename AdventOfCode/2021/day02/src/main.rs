fn main() {
    let file = include_str!("../inputs/2.txt");
    let lines: Vec<(&str, i32)> = file
        .lines()
        .map(|l| {
            let (action, number_str) = l.split_once(" ").unwrap();
            let number = number_str.parse().unwrap();
            (action, number)
        })
        .collect();

    // println!("{:?}", lines);

    // [ PART 1 ]
    let (f, d) = lines
        .iter()
        .fold((0, 0), |(f, d), &(k, v)| {
            match (k, v) {
                ("forward", v) => (f+v, d),
                ("down", v) => (f, d+v),
                ("up", v) => (f, d-v),
                _ => unreachable!(),
            }
        });
    println!("Part 1: {}", f*d);

    // [ PART 2 ] h: horizontal; d: depth; a: aim
    let (h, p, _) = lines
        .iter()
        .fold((0, 0, 0), |(h, p, a), &(m, n)| {
            match (m, n) {
                ("forward", n) => (h + n, p + a*n, a),
                ("down", n) => (h, p, a + n),
                ("up", n) => (h, p, a - n),
                _ => unreachable!(),
            }
        });

    // println!("{} {} ", h, p);
    println!("Part 2: {}", h*p);

}
