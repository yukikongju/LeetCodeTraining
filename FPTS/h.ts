// incrementing number
type Increment = (x: number) => number;
const increment: Increment = (x) => x + 1;

console.log(increment(2));

// to string
type ToString = (x: number) => string;
const tostring: ToString = (x) => `"${x}"`;
console.log(tostring(2));

// function composition
type IncrementThenToString = (x: number) => string;
const incrementThenToString: IncrementThenToString = (x) =>
  tostring(increment(x));
console.log(incrementThenToString(4));

// general function composition: f(g(x))
// type Compose = (
//   f: (x: number) => string,
//   g: (x: number) => number
// ) => (x: number) => string;
// const compose: Compose = (f, g) => (x) => f(g(x));

// general function composition: f(g(x)) with generics
type Compose = <A, B, C>(f: (x: B) => C, g: (x: A) => B) => (x: A) => C;
const compose: Compose = (f, g) => (x) => f(g(x));

// define incrementThenToString2 with Compose
const incrementThenToString2: IncrementThenToString = compose(
  tostring,
  increment
);
console.log(incrementThenToString2(8));
