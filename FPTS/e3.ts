// e3 - Compute first 8 fibonacci numbers

// import { Eitherz, leftz, rightz } from "./e2";
type Eitherz<L, R> = Leftz<L> | Rightz<R>;
interface Leftz<L> {
  _tag: "leftz";
  value: L;
}
interface Rightz<R> {
  _tag: "rightz";
  value: R;
}
const leftz = <L, R = never>(l: L): Eitherz<L, R> => ({
  _tag: "leftz",
  value: l,
});
const rightz = <R, L = never>(r: R): Eitherz<L, R> => ({
  _tag: "rightz",
  value: r,
});

// type Fibonacci = (x: number) => Eitherz<string, number>;
// const fibonacci: Fibonacci = (x) => {
//   if (x < 0) {
//     return leftz("undefined");
//   } else if (x == 0) {
//     return rightz(0);
//   } else if (x == 1) {
//     return rightz(1);
//   } else if (x == 2) {
//     return rightz(1);
//   } else {
//     return rightz(fibonacci(x - 1) + fibonacci(x - 2));
//   }
// };
