// --- implementing List, cons, nil, match
type Listz<A> = Nilz | Consz<A>;
interface Nilz {
  _tag: "Nilz";
}
interface Consz<A> {
  _tag: "Consz";
  head: A;
  tail: Listz<A>;
}
const nilz: Listz<never> = { _tag: "Nilz" };
const consz = <A>(head: A, tail: Listz<A>): Listz<A> => ({
  _tag: "Consz",
  head: head,
  tail: tail,
});
const isNilz = <A>(xs: Listz<A>): xs is Nilz => xs._tag === "Nilz";

type MatchL = <A, B>(
  onNil: () => B,
  onCons: (head: A, tail: Listz<A>) => B
) => (xs: Listz<A>) => B;
const matchL: MatchL = (onNil, onCons) => (xs) =>
  isNilz(xs) ? onNil() : onCons(xs.head, xs.tail);

// const tListz: Listz<number> = nilz;
const tmatch = matchL(
  () => `test list empty`,
  (head: number, tail: Listz<number>) => `head is ${head}`
);
console.log(tmatch(nilz));
const tList: Listz<number> = consz(5, consz(6, consz(4, nilz)));
console.log(tmatch(tList));

// --- implement addAll(), multiplyAll() and appendAll()

type AddAll = (xs: Listz<number>) => number;
// const addAll = (xs) =>
//   matchL(
//     () => 0,
//     (head: number, tail: Listz<number>) => head + addAll(tail)
//   )(xs);
const addAll = matchL(
  () => 0,
  (head: number, tail: Listz<number>) => head + addAll(tail)
);
console.log(addAll(tList));

type MultiplyAll = (xs: Listz<number>) => number;
const multiplyAll = matchL(
  () => 1,
  (head: number, tail: Listz<number>) => head * multiplyAll(tail)
);
console.log(multiplyAll(tList));

type AppendAll = (xs: Listz<string>) => string;
const appendAll = matchL(
  () => ``,
  (head: string, tail: Listz<string>) => head + appendAll(tail)
);

// convert List of Number to List of string
type ConvertListNumToListString = (xs: Listz<number>) => Listz<string>;
const convertListNumToListString = matchL(
  () => nilz,
  (head: number, tail: Listz<number>) =>
    consz(`${head}`, convertListNumToListString(tail))
);
console.log(convertListNumToListString(tList));
console.log(appendAll(convertListNumToListString(tList)));

// --- Magma, Semigroup
interface Magma<A> {
  concat: (x: A, y: A) => A;
}

interface Semigroup<A> extends Magma<A> {}

const addSemigroup: Semigroup<number> = { concat: (x, y) => x + y };
const multiplySemigroup: Semigroup<number> = { concat: (x, y) => x * y };
const concatSemigroup: Semigroup<string> = { concat: (x, y) => x.concat(y) };

const concatAll =
  <A>(s: Semigroup<A>) =>
  (neutral: A) =>
  (xs: Listz<A>): A =>
    matchL(
      () => neutral,
      (head: A, tail: Listz<A>) => s.concat(head, concatAll(s)(neutral)(tail))
    )(xs);

console.log(concatAll(addSemigroup)(0)(tList));
console.log(concatAll(multiplySemigroup)(1)(tList));
console.log(concatAll(concatSemigroup)("")(convertListNumToListString(tList)));

// Monoid

interface Monoid<A> extends Semigroup<A> {
  neutral: A;
}

const addMonoid: Monoid<number> = { ...addSemigroup, neutral: 0 };
const multiplyMonoid: Monoid<number> = { ...multiplySemigroup, neutral: 1 };
const concatMonoid: Monoid<string> = { ...concatSemigroup, neutral: "" };

const concatAllMonoid =
  <A>(m: Monoid<A>) =>
  (xs: Listz<A>): A =>
    matchL(
      () => m.neutral,
      (head: A, tail: Listz<A>) => m.concat(head, concatAllMonoid(m)(tail))
    )(xs);
console.log(concatAllMonoid(addMonoid)(tList));
console.log(concatAllMonoid(multiplyMonoid)(tList));
