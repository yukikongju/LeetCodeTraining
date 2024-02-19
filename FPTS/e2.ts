// ex2 - write a function that function that returns Either on square root

console.log(Math.sqrt(-1)); // NaN

// define complex type
// type Complex<I, R> = Imaginary<I> | Real<R>;
// interface Imaginary<I> {
//   _tag: "Imaginary";
//   value: I;
// }
// interface Real<R> {
//   _tag: "Real";
//   value: R;
// }

// const imaginary = <I, R = never>(i: I): Complex<I, R> => ({
//   _tag: "Imaginary",
//   value: i,
// });
// const real = <R, I = never>(r: R): Complex<I, R> => ({
//   _tag: "Real",
//   value: r,
// });

// define Either type

//

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

function square_root(x: number): Eitherz<string, number> {
  if (x < 0) {
    return leftz("i");
  } else {
    return rightz(Math.sqrt(x));
  }
}
console.log(square_root(2));
console.log(square_root(0));
console.log(square_root(-3));
