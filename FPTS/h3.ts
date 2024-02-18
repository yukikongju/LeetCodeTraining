// DivideTwo function
type DivideTwo = (x: number) => number;
const divideTwo: DivideTwo = (x) => 2 / x;

console.log(divideTwo(1));
console.log(divideTwo(0)); // Infinity

// Increment Divide Two function

// composition(f, g) = f(g(x))
type Composition1 = <A, B, Z>(f: (x: B) => Z, g: (x: A) => B) => (x: A) => Z;
const composition1: Composition1 = (f, g) => (x) => f(g(x));

// curry(x)(y) = f(x, y)
type Curry1 = <A, B, Z>(f: (x: A, y: B) => Z) => (x: A) => (y: B) => Z;
const curry1: Curry1 = (f) => (a) => (b) => f(a, b);

// sum(x)(y)
type Sum0 = (x: number) => (y: number) => number;
const sum0: Sum0 = (x) => (y) => x + y;
console.log(sum0(5)(2));

type Increment0 = (x: number) => number;
const increment0: Increment0 = (x: number) => sum0(x)(1);
console.log(increment0(8));

const divideTwoIncrement = composition1(increment0, divideTwo);
console.log(divideTwoIncrement(2)); // (2 / 2) + 1
console.log(divideTwoIncrement(0)); // we see what error is propagated because we are dealing with partial function

// Defining Option Type

type Option<A> = Some<A> | None;
interface Some<A> {
  _tag: "Some";
  value: A;
}
interface None {
  _tag: "None";
}
const some = <A>(x: A): Option<A> => ({ _tag: "Some", value: x });
const none: Option<never> = { _tag: "None" };

const isNone = <A>(x: Option<A>): x is None => x._tag === "None";

type DivideTwo2 = (x: number) => Option<number>;
const divideTwo2: DivideTwo2 = (x) => (x === 0 ? none : some(2 / x));
console.log(divideTwo2(2));
console.log(divideTwo2(0));
