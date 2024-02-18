// --- Ex0: Map, Filter, Reduce Accumulate in TS
// https://www.crocoder.dev/blog/map-filter-reduce-exercises/

// e0 - array squared (x)
const myTuple = [1, 2, 3, 4, 5, 6, 7, 8];
const array_squared = myTuple.map((x) => x * x);
// console.log(array_squared);

// e1 - sum of every positive elements (x)
const myTuple1 = [1, -4, 12, 0, -3, 29, -150];
const sum_of_positive_elements = myTuple1
  .filter((x) => x > 0)
  .reduce((accumulator, val) => {
    return accumulator + val;
  });
// console.log(sum_of_positive_elements);

// e2 - calculate mean (x) and median (todo)
const mean =
  myTuple.reduce((acc, val) => {
    return acc + val;
  }) / myTuple.length;
// console.log(mean);

// e3 - get name initials (x)
const s = "George Raymond Richard Martin";
const abbrev = s
  .split(" ")
  .map((x) => {
    return x[0];
  })
  .join("");
// console.log(abbrev);

// e4 - compute diff points between males and females: females points x1.5 (x)
const players = [
  { name: "John", sex: "M", points: 13 },
  { name: "Mark", sex: "M", points: 56 },
  { name: "Rachel", sex: "F", points: 45 },
  { name: "Nate", sex: "M", points: 67 },
  { name: "Jennifer", sex: "F", points: 65 },
];
const points_diff = players.reduce((acc, x) => {
  return x.sex === "F" ? acc - x.points * 1.5 : acc + x.points;
}, 0);
// console.log(points_diff);

// e5 - first n factorial (todo)

// e6 - count elements in array of arrays (x);
const elements = [
  ["a", "b", "c"],
  ["c", "d", "f"],
  ["d", "f", "g"],
];
// in version later than es2019: use flat()
const counter: Record<string, number> = elements
  .reduce((acc, val) => acc.concat(val), [])
  .reduce((acc, val) => {
    acc[val] = acc[val] ? acc[val] + 1 : 1;
    return acc;
  }, {});
// const sortedCounter = Object.entries(counter).sort((a, b) => b[1] - a[1]); // only works for >= es2017
// console.log(counter);

// e7 - filter students with grade above 88 weighted by exam ponderation (x)
const ponderations = [0.2, 0.3, 0.5];
const students = [
  { name: "Alice", scores: [90, 85, 92] },
  { name: "Bob", scores: [75, 80, 85] },
  { name: "Charlie", scores: [90, 95, 85] },
  { name: "Jack", scores: [100, 100, 100] },
];
const high_grades = students
  .map((x) => {
    const grade = x.scores.reduce((acc, val, i) => {
      return acc + val * ponderations[i];
    }, 0);
    return { name: x.name, scores: x.scores, grade: grade };
  })
  .filter((x) => x.grade > 88);
// console.log(high_grades);

// e8 - compute payroll by departments (todo)
const employees = [
  { name: "John", salary: 50000, department: "IT" },
  { name: "Jane", salary: 60000, department: "HR" },
  { name: "Bob", salary: 55000, department: "IT" },
  { name: "Sophie", salary: 75000, department: "HR" },
  { name: "Mike", salary: 65000, department: "IT" },
  { name: "Emily", salary: 80000, department: "HR" },
  { name: "David", salary: 70000, department: "IT" },
];
const payrolls = employees.reduce((acc, x) => {
  acc[x.department] = acc[x.department]
    ? acc[x.department] + x.salary
    : x.salary;
  return acc;
}, {});
console.log(payrolls);
