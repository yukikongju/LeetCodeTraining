# Learn You Haskell

[link](http://learnyouahaskell.com/chapters)

## Contents

- [X] Chapter 1 - Introduction
- [X] Chapter 2 - Starting Out
    - [X] Ready, Set, Go!
    - [X] Baby's First Functions
    - [X] An Intro to list
    - [X] Texas Range
    - [X] I'm a list comprehension
    - [X] Tuples
- [X] Chapter 3 - Types and Typeclasses
    - [X] Believe the type
    - [X] Type Variables
    - [X] Typeclasses 101
- [ ] Chapter 4 - Syntax in Functions
    - [ ] Pattern Matching
    - [ ] Guards, guards!
    - [ ] Where?!
    - [ ] Let it be
    - [ ] Case expressions
- [ ] Chapter 5 - Recursion
- [ ] Chapter 6 - Higher Order Functions
- [ ] Chapter 7 - Modules
- [ ] Chapter 8 - Making our own types and typeclasses
- [ ] Chapter 9 - Input and Output  
- [ ] Chapter 10 - Functionally Solving Problems
- [ ] Chapter 11 - Functors, Applicative Functors and Monoids
- [ ] Chapter 12 - A Fistful Monads
- [ ] Chapter 13 - For a Few Monads More
- [ ] Chapter 14 - Zippers

### 1. Introduction

Blabla

### 2. Starting Out

**Ready, set, go!**

- using `ghci`
- using arithmetic operations `+-*/`
- using boolean operations `||`, `&&`, `not`
- testing for inequality with `==` and `=\`
- the functions `succ`, `max`, `min`

**Baby's first functions**

- saving code using `:l <file_name>.hs`
- declaring a function: `<func_name> <arg1> ... <argn> = ...`
- If-then-else

**An Intro to lists**

- creating a list with `let <list_name> = [...]`
- concatenating with `++` and `'item':<list_name>` (and why ++ is slower)
- lists indexing with `<list_name> !! <index>`
- built-in lists functions: `head`, `tail`, `last`, `init`, `length`, `null`, `reverse`, `take`, `drop`, `maximum`, `minimum`, `sum`, `product`, `elem`

**Texas Range**

- creating a int list in range `[<start>, <inc>..<end>]`
- why range shouldn't be used with floats
- combining `take` with `cycle`, `repeat`, `replicate`

**I'm a list comprehension**

- list comprehension create all combinations: `[ <operations> | <variable init and conditions> ]`

**Tuples**

- using the built-in tuple functions `fst`, `snd`, `zip`
- using tuple with list comprehension

### Chapter 3 - 

**Believe the type**

- print a variable type with `:t <variable>`
- declaring function types with `<function_name> <arg1> :: <arg1_type> -> <return type>`
- Different types: `Int`, `Integer`, `Float`, `String`, `Char`, `Bool`

**Type Variables**

- functions that have type variables are called `polymorphic functions`

**Typeclasses 101**

- "Interfaces": `Eq`, `Ord`, `Show`, `Read`, `Enum`, `Bounded`, `Num`, `Integral`, `Floating`

### Chapter 4 - 

**Pattern Matching**

- declaring recursive function using integral: `lucky :: (Integral a) => a -> String`

**Guards, guards!**

**Where?!**

**Let it be**

**Case expressions**

