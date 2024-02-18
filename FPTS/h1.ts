// declarative function
function normal_sum(a, b) {
  return a + b;
}

console.log(normal_sum(1, 2));

// make function unary
// function sum(a) {
//   return function (b) {
//     return a + b;
//   };
// }
// console.log(sum(1)(5));

// define unary function with type
type Sum = (a: number) => (b: number) => number;
const sum: Sum = (a) => (b) => a + b;
console.log(sum(1)(5));

// define function with the same binary operator +
type Increment = (a: number) => number;
const increment: Increment = sum(1);
const incrementBy10: Increment = sum(10);
const decrement: Increment = sum(-1);
console.log(incrementBy10(2));
console.log(decrement(2));

// define general curry function
// type Curry = (
//   f: (a: number, b: number) => number
// ) => (a: number) => (b: number) => number;
type Curry = <A, B, Z>(f: (a: A, b: B) => Z) => (a: A) => (b: B) => Z;
const curry: Curry = (f) => (a) => (b) => f(a, b);
const sum2 = curry(normal_sum);
console.log(sum2(1)(2));
