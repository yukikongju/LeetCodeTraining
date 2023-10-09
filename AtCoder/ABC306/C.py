#  https://atcoder.jp/contests/abc306/tasks/abc306_c
#  !python3 % < AtCoder/ABC306/inputs/c1.in;

from collections import defaultdict

# --- 1. read inputs
N = int(input())
A = list(map(int, input().split()))

# --- 2. 

# - build index list for each numbers
orders = defaultdict(list)
for i, a in enumerate(A):
    orders[a].append(i+1)

# - build B array such that [(f(a_i), a_i), ..., ]
B = [ (orders[i][1], i) for i in range(1, N+1) ]

# - sort
B.sort(key=lambda x: x[0])

# --- 3. print
for f, a in B: print(a, end=' ')

