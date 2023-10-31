from collections import defaultdict

n = int(input())
socks = list(map(int, input().split()))

counts = defaultdict(int)
for sock in socks:
    counts[sock] += 1

total = 0
for key, value in counts.items():
    total += value // 2

print(total)
