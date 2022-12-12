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

>>> substring :: String -> Int -> Int 
>>> substring string start end = 
    take (end - start + 1) (drop start string)


-- [> Write a function which takes a list of integer and returns the square of all odd number
-- >>> squareOfOdds [1..10] 
-- >>> [1,9,25,49,81]
-- <]

>>> squareOfOdds :: [Int] -> [Int]
>>> squareOfOdds list = 
    [x * x | x <- list, (mod x 2) == 1]

-- [> Create a list that combines all nouns and adjectives combination from a list of noun and a list of adjective <]

>>> concatNounAdjective nouns adjectives :: [String] -> [String] -> [String]
>>> concatNounAdjective nouns adjectives = 
    [ noun ++ " " ++ adjective | noun <- nouns, adjective <- adjectives ]

-- [> Write a function which takes 3 list of integers and return a list of all 
-- valid triangles<]

>>> triangles :: [Int] -> [Int] -> [Int] -> (Int, Int, Int)
>>> triangles as bs cs = [(a, b, c) | a <- as, b <- bs, c <- cs, a^2 + b^2 == c^2]


-- [> | Write a function that takes a String — space separated numbers, and finds a sum of the numbers inside this string.

TODO


{- | Write a function that takes a number and a list of numbers and
returns a string, saying how many elements of the list are strictly
greater than the given number and strictly lower.
>>> lowerAndGreater 3 [1 .. 9]
"3 is greater than 2 elements and lower than 6 elements" -}


TODO

