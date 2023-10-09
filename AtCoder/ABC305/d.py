# https://atcoder.jp/contests/abc305/tasks/abc305_d
# !python3 % < AtCoder/ABC305/inputs/d1.in;

# --- 1. read inputs
N = int(input())
A = [int(a) for a in input().split()]
Q = int(input())
questions = [tuple(map(int, input().split())) for _ in range(Q)]

# --- 2. compute intervals
intervals = [(A[i], A[i+1]) for i in range(1, N, 2)]

sols = []
for l1, r1 in questions:
    duration = 0
    for l2, r2 in intervals:
        if l2 >= r1:
            break
        if l2 < r1:
            duration += min(r1, r2) - max(l1, l2)
    sols.append(duration)

# --- 3. print answers
for sol in sols: print(sol)

