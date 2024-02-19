// e0 - write a function that transform a list of Celsius into Fahrenheit and print it

// --- compose: (f, g)(x) = f(g(x))
type Composee = <A, B, Z>(f: (x: B) => Z, g: (x: A) => B) => (x: A) => Z;
const composee: Composee = (f, g) => (x) => f(g(x));

// --- curry: f(x, y) = (f)(x)(y)
type Currie = <A, B, Z>(f: (x: A, y: B) => Z) => (x: A) => (y: B) => Z;
const currie: Currie = (f) => (x) => (y) => f(x, y);

// type Add = <A>(x: A) => (y: A) => A;
type Add = (x: number) => (y: number) => number;
const add: Add = (x) => (y) => x + y;
const incrementz = add(1);

type ToStringz = <A>(x: A) => string;
const toStringz: ToStringz = (x) => `"${x}"`;
const printIncrement = composee(toStringz, incrementz);
// console.log(printIncrement(5));

//
function celciusToFahrenheit(x: number): number {
  return x * 1.8 + 32;
}
// type PrintConversion = <A, B>(
//   f: (x: A) => B,
//   t1: string,
//   t2: string
// ) => (x: A) => string;

type PrintConversion = (
  f: (x: number) => number,
  t1: string,
  t2: string
) => (x: number) => string;

type NumberFormat = (x: number) => (y: number) => string;
const numberFormat: NumberFormat = (x) => (y) => Number(y).toFixed(x);
const format2Digits = numberFormat(2);
// console.log(format2Digits(2.345678765));
// console.log(Number(2.345678765).toFixed(2));

const printConversion: PrintConversion = (f, t1, t2) => (x) =>
  `"${format2Digits(x)} ${t1} => ${format2Digits(f(x))} ${t2}"`;
const printCelsiusToFahreinheit = printConversion(
  celciusToFahrenheit,
  "C",
  "F"
);
console.log(printCelsiusToFahreinheit(30));

//
const weeklyDegrees = [15, 21, 26, 14, 23.5, 32, 29];
// type PrintListCelsiusToFahreinheitConversion = <A,B>(f: (x: A) => B) => string;
type PrintListCelsiusToFahreinheitConversion = (xs: number[]) => string;
const printListCelsiusToFahreinheitConversion: PrintListCelsiusToFahreinheitConversion =
  (xs) => {
    if (xs.length == 0) {
      return "";
    }
    const [head, ...rest] = xs;
    return (
      printCelsiusToFahreinheit(head) +
      "\n" +
      printListCelsiusToFahreinheitConversion(rest)
    );
  };
console.log(printListCelsiusToFahreinheitConversion(weeklyDegrees));
