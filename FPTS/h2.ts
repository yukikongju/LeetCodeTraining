// sum all in imperative programming
function normal_sum_all(xs: number[]): number {
  let result = 0;
  for (let i = 0; i <= xs.length; i++) {
    result += xs[i];
  }
  return result;
}

function is_even(x: number): boolean {
  return x % 2 == 0;
}

function add_normal(a: number, b: number): number {
  return a + b;
}

// sum all fp: recursive
type SumAll = (xs: number[]) => number;
const sum_all: SumAll = (xs) => {
  if (xs.length == 0) {
    return 0;
  }
  const [head, ...rest] = xs;
  return head + sum_all(rest);
};
console.log(sum_all([1, 2, 3, 4]));

// sum all fp: recursive (short version)
const sum_all2: SumAll = (xs) =>
  xs.length == 0 ? 0 : xs[0] + sum_all2(xs.slice(1));
console.log(sum_all2([1, 2, 3, 4]));

// Exo: combine with function composition and function curry: check if sum all is even and print
type Curry2 = <A, B, Z>(f: (a: A, b: B) => Z) => (a: A) => (b: B) => Z;
const curry2: Curry2 = (f) => (a) => (b) => f(a, b);

type Composition = <A, B, Z>(f: (b: B) => Z, g: (a: A) => B) => (a: A) => Z;
const composition: Composition = (f, g) => (x) => f(g(x));

// ---
const isSumAllAdd50Even = composition(
  is_even,
  (curry2(add_normal)(50), sum_all)
);

console.log(isSumAllAdd50Even([1, 2, 3, 4]));
