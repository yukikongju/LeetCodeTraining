🟩 1. Basic Prefix Sum

Compute running totals or subarray sums.

✔ Must-Solve

Running Sum of 1d Array

Range Sum Query – Immutable

Subarray Sum Equals K

Maximum Subarray Sum of Size K

Core Pattern

prefix[i] = prefix[i-1] + nums[i]

Subarray sum [i, j] = prefix[j] - prefix[i-1]

Use hashmap for counting prefix sums

🟦 2. 2D Prefix Sum / Matrix Sum

Sum of submatrices in 2D arrays.

✔ Must-Solve

Range Sum Query 2D – Immutable

Maximum Sum Rectangle in 2D Matrix

Num Matrix with Updates (Mutable)

Submatrix Sum Equals K

Core Pattern

prefix[i][j] = matrix[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

Sum of submatrix using 4 corners

Convert 2D to 1D for some problems (Kadane variant)

🟥 3. Mod / Remainder Problems

Use prefix sum modulo to detect subarrays with certain properties.

✔ Must-Solve

Subarray Sum Divisible by K

Continuous Subarray Sum

Count Number of Nice Subarrays

Subarray Sums Divisible by M

Core Pattern

Compute prefix[i] % k

Use hashmap to count same remainders

Number of valid subarrays increases when remainder repeats

🟨 4. Sliding Window + Prefix Sum

Optimize sum computation in a window.

✔ Must-Solve

Maximum Sum of Subarray of Size K

Minimum Size Subarray Sum

Number of Subarrays with Sum at Most K

Sum of All Odd Length Subarrays

Core Pattern

Use prefix sum to get window sum in O(1)

Combine with two pointers or sliding window

Efficiently move left and right pointers

🟪 5. Prefix XOR

Prefix XOR is like prefix sum but for XOR operations.

✔ Must-Solve

Maximum XOR of Two Numbers in Array

Subarray XOR Equals K

Count Triplets With XOR 0

XOR Queries of a Subarray

Core Pattern

prefixXOR[i] = prefixXOR[i-1] ^ nums[i]

Subarray XOR [i, j] = prefixXOR[j] ^ prefixXOR[i-1]

Use hashmap for counting or trie for max XOR

🟫 6. Prefix Sum on Strings

Treat strings like numbers or characters.

✔ Must-Solve

Number of Substrings Containing All Three Characters

Count Binary Substrings

Minimum Add to Make Parentheses Valid

Longest Balanced Substring

Core Pattern

Map characters to numeric values

Compute running totals

Use hashmap or array for counts

🟧 7. Cumulative / Difference Array

Used for range updates and queries efficiently.

✔ Must-Solve

Corporate Flight Bookings (Range Add)

Car Pooling (Range Sum)

Car Pooling II (Prefix + Sliding Window)

Range Addition / Range Increment Queries

Core Pattern

diff[i] = arr[i] - arr[i-1]

Add value to diff[l] and subtract at diff[r+1]

Compute final array with cumulative sum

⭐ Top 15 Prefix Sum Problems (Interview Must-Know)

Running Sum of 1d Array

Subarray Sum Equals K

Maximum Sum Subarray of Size K

Range Sum Query – Immutable

Range Sum Query 2D – Immutable

Maximum Sum Rectangle in 2D Matrix

Subarray Sum Divisible by K

Continuous Subarray Sum

Count Number of Nice Subarrays

Sum of All Odd Length Subarrays

Minimum Size Subarray Sum

XOR Queries of a Subarray

Maximum XOR of Two Numbers in Array

Count Triplets With XOR 0

Corporate Flight Bookings
