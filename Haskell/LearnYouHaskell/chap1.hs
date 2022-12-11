-- Exercices taken from: https://github.com/haskell-beginners-2022/exercises/blob/main/src/Lecture1.hs


-- [> | Implement a function that takes two numbers and finds sum of their squares.

>>> sumOfSquares x y = x*x + y*y

-- [> | Implement a function that returns the last digit of a given number.

>>> lastDigit x = mod x 10

-- [> | Write a function that takes three numbers and returns the difference between the biggest number and the smallest one.

>>> minmax x y z =
    let list = [x, y, z]
     in maximum(list) - minimum(list)

-- [>  | Implement a function that takes a string, start and end positions and returns a substring of a given string from the start position to the end (including).  <]

TODO

-- >>> substring start end string = 

-- [> | Write a function that takes a String — space separated numbers, and finds a sum of the numbers inside this string.

TODO


{- | Write a function that takes a number and a list of numbers and
returns a string, saying how many elements of the list are strictly
greater than the given number and strictly lower.
>>> lowerAndGreater 3 [1 .. 9]
"3 is greater than 2 elements and lower than 6 elements" -}


TODO

