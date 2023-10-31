# idea: if a digit occurs two times, we can reduce it

from collections import defaultdict

S = input()

digits = [0]*10
counts = defaultdict(int)
counts[tuple(digits)] = 1
for s in S:
    x = int(s)
    digits[x] += 1
    digits[x] %= 2
    if tuple(digits) in counts:
        counts[tuple(digits)] += 1
    else:
        counts[tuple(digits)] = 1

total = 0
for k, v in counts.items(): # n(n-1) / 2
    total += v*(v-1) // 2

print(total)
