// Ex: implement divideTwoIfEven using Either
function divideTwoIfEven(x: number): number {
  if (x === 0) {
    throw "cannot divide by 0";
  } else if (x % 2 !== 0) {
    throw "num is not even";
  } else {
    return 2 / x;
  }
}

// defining "Either" type
type Either<E, A> = Left<E> | Right<A>;
interface Left<E> {
  _tag: "left";
  left: E;
}
interface Right<A> {
  _tag: "right";
  right: A;
}
const left = <E, A = never>(e: E): Either<E, A> => ({
  _tag: "left",
  left: e,
});
const right = <A, E = never>(a: A): Either<E, A> => ({
  _tag: "right",
  right: a,
});

// defining the function with Either Type
function divideTwoIfEven2(x: number): Either<string, number> {
  if (x === 0) {
    return left("division by 0");
  } else if (x % 2 !== 0) {
    return left("x not even");
  } else {
    return right(2 / x);
  }
}
console.log(divideTwoIfEven2(0));
console.log(divideTwoIfEven2(3));
console.log(divideTwoIfEven2(6));
