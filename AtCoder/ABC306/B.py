# https://atcoder.jp/contests/abc306/tasks/abc306_b
#  !python3 % < AtCoder/ABC306/inputs/b1.in;

# --- 1. read inputs
A = list(map(int, input().split()))

# --- 2.
total = 0
for i, a in enumerate(A):
    if a: total += a * (1<<i)

# --- 3.
print(total)

