# Functional Programming in TypeScript


## Concepts Learned

- [X] Function Composition: `h.ts`
	- define template to be reused with generics
- [X] Function Currying: `h1.ts`
	- use unary function to define function with same operator (increment, 
	  increment by 10)
- [X] Function Recursion: `h2.ts`
	- no loop; define base case
- [X] Option, Maybe and null value: `h3.ts`
	- partial vs total function
	- Option: None or Some
- [X] Either: `h4.ts`
	- Either: Left | Right
- [X] List, Linked List: `h5.ts`
- [X] ADT, Pattern Matching: `h6.ts`
	- ADT: algebraic data type is a composition data type using operation PRODUCT or SUM
	- Product Type: cardinality is product of both types
	- Sum Type and variant // CoProduct // Tagged // Disjoint Union: cardinality is sum of both type
	- Pattern matching should cover all the values
- [X] Magma, Semigroup, Monoid: `h7.ts`
	- `point free form`
- [ ] Group: `h8.ts`
- [ ] Functor: `h9.ts`
- [ ] Higher-order function
- [ ] type class in fp-ts: `h10.ts`

Definitions:
* Unary Functions: function with one parameter
* array restructuring: `const [head, ...rest]=xs`, where `xs: number[]`

**Exercices**

- [X] 0 Map, Filter, Reduce, Accumulate =>
- [X] 1 Function Composition + Currying => write a function that transform a list of Celsius into Fahrenheit and print it
- [X] 2 Partial Function => write a function that return Either when applied to square root
- [ ] 3 Recursion => Compute the first 8 fibonacci numbers
- [ ] 4 Linked List => Compute the Sum of head until current node and print it
- [ ] 5 
- [ ] 6 
- [ ] 7 
- [ ] 8 


## code

Running TypeScript code locally

```
npm install -g ts-node typescript '@types/node'
make run
```

## Ressources

- [ ] [Web Village Voyage - Functional Programming with TypeScript](https://www.youtube.com/playlist?list=PLuPevXgCPUIMbCxBEnc1dNwboH6e2ImQo)
- [ ] [MrFunctor - fp-ts Tutorial](https://www.youtube.com/playlist?list=PLUMXrUa_EuePN94nJ2hAui5nWDj8RO3lH)
- [ ] [fp-ts Learning Ressources](https://gcanti.github.io/fp-ts/learning-resources/)
- [ ] [mostly-adequate-guide](https://mostly-adequate.gitbook.io/mostly-adequate-guide/)
