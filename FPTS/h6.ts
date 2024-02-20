// --- re-implement option

type Optionz<A> = Nil | Somz<A>;
interface Nil {
  _tag: "Nil";
}
interface Somz<A> {
  _tag: "Some";
  value: A;
}

// note: nil is a primitive so it takes '=' where as
// somz is a function that wraps any value
const nil: Optionz<never> = { _tag: "Nil" };
const somz = <A>(x: A): Optionz<A> => ({ _tag: "Some", value: x });
const isNil = <A>(x: Optionz<A>): x is Nil => x._tag === "Nil";

// --- OPTION => "Match" W Implementation -
// exp: convert type A to type B with Option

type Match = <A, B>(
  onNil: () => B,
  onSomz: (x: A) => B
) => (x: Optionz<A>) => B;
const match: Match = (onNil, onSomz) => (x) =>
  isNil(x) ? onNil() : onSomz(x.value);
const maybeNum: Optionz<number> = somz(12);
const result = match(
  () => `num doesn't exist`,
  (a: number) => `num is ${a}`
)(maybeNum);
console.log(result);

// --- EITHER => "Match" with "Either" -
// expl:

type Eitherz<L, R> = Leftz<L> | Rightz<R>;
interface Leftz<L> {
  _tag: "left";
  left: L;
}
interface Rightz<R> {
  _tag: "right";
  right: R;
}

// leftz and rightz are functions
const leftz = <L, R = never>(l: L): Eitherz<L, R> => ({
  _tag: "left",
  left: l,
});
const rightz = <R, L = never>(r: R): Eitherz<L, R> => ({
  _tag: "right",
  right: r,
});
const isRight = <L, R>(x: Eitherz<L, R>): x is Rightz<R> => x._tag === "right";

type MatchE = <L, R, Z>(
  onLeft: (l: L) => Z,
  onRight: (r: R) => Z
) => (x: Eitherz<L, R>) => Z;
const matchE: MatchE = (onLeft, onRight) => (x) =>
  isRight(x) ? onRight(x.right) : onLeft(x.left);
const errorOrNum = matchE(
  (e: string) => `Error happened: ${e}`,
  (x: number) => `Number is ${x}`
);

const t1: Eitherz<string, number> = leftz("bad input");
console.log(errorOrNum(t1));
const t2: Eitherz<string, number> = rightz(19);
console.log(errorOrNum(t2));

// --- TODO: List
// expl:
