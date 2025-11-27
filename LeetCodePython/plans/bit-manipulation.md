# Bit Manipulation

🟩 1. Single Number / XOR Trick

Classic use of XOR to find unique elements.

✔ Must-Solve

Single Number (Find element appearing once)

Single Number II (Every element appears 3 times except one)

Missing Number

Find the Duplicate Number (bitwise approach)

XOR of All Numbers in Range

Core Idea

XOR of a number with itself → 0

XOR with 0 → number itself

XOR is commutative and associative

🟦 2. Counting Bits / Set Bits / Population Count

Problems where you count 1s in binary.

✔ Must-Solve

Number of 1 Bits (Hamming Weight)

Counting Bits (0…n)

Hamming Distance

Total Hamming Distance

Reverse Bits

Bitwise AND of Numbers Range

Core Idea

Use n & (n-1) trick to remove lowest set bit

DP to build up counts

XOR to find differences

🟥 3. Subsets / Power Set via Bits

Generate subsets using binary representation.

✔ Must-Solve

Subsets (iterative via bits)

Subsets II (handle duplicates)

Letter Tile Possibilities (optional)

Maximum XOR of Two Numbers in an Array

Core Idea

Treat an integer from 0 → 2^n - 1 as subset mask

If bit i is 1 → include nums[i]

🟨 4. Bitmask DP / State Compression

For more advanced problems with constraints.

✔ Must-Solve

Partition to K Equal Sum Subsets (bitmask DP)

Traveling Salesman Problem (TSP)

Smallest Sufficient Team

Maximum Compatibility Score

Word Squares (with mask)

Count Numbers With Unique Digits

Core Idea

Use bits to represent “picked items” or “states”

DP[state] → result of this combination

🟪 5. Bitwise Operations / Manipulations

Direct manipulation problems.

✔ Must-Solve

Reverse Bits

Number Complement

Power of Two / Power of Four / Power of Eight

Bitwise AND of Numbers Range

Sum of Two Integers (without + or -)

Divide Two Integers (bitwise shift)

Missing Number

Core Idea

Shifts, XOR, AND, OR, NOT for calculations

Often avoids loops or extra space

🟫 6. Subsets of Size k / Combinations using Bits

Use bitmask to enumerate combinations of size k.

✔ Must-Solve

Combinations (n choose k)

Letter Tile Possibilities

Maximal XOR of subsets

Core Idea

Filter subsets with bin(mask).count('1') == k

🟧 7. Advanced / Trick Problems

Problems with clever bit tricks or optimization.

✔ Must-Solve

Maximum XOR of Two Numbers in an Array (Trie + bits)

Single Number II (sum of bits modulo 3)

Find Missing and Duplicate Number

Number of Wonderful Substrings (parity mask)

Minimum XOR of Two Arrays

Core Idea

XOR and bit masks to encode problem state

Sum bits to extract counts modulo some number

🟦 8. Greedy + Bits

Use bit properties to optimize greedy.

✔ Must-Solve

Maximum XOR of Two Numbers

Bitwise AND of Subsets

Subset XOR Totals

⭐ Top 20 Bit Manipulation Problems (Must-Know)

Single Number

Single Number II

Missing Number

Hamming Weight / Distance

Counting Bits

Bitwise AND of Numbers Range

Reverse Bits

Number Complement

Power of Two / Four

Sum of Two Integers

Divide Two Integers

Maximum XOR of Two Numbers

Subsets

Subsets II

Letter Tile Possibilities

Partition to K Equal Sum Subsets (bitmask DP)

Smallest Sufficient Team

XOR of All Numbers in Range

Count Numbers with Unique Digits

Minimum XOR of Two Arrays
