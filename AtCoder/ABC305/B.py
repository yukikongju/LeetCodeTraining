#  https://atcoder.jp/contests/abc305/tasks/abc305_b

# --- 1. read inputs

P, Q = input().split()

# --- 2. 
distances = {'A': 0, 'B': 3, 'C': 4, 'D': 8, 'E': 9, 'F': 14, 'G': 23}
dist = abs(distances[P] - distances[Q])
print(dist)

