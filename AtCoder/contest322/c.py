#  !python3 % < AtCoder/contest322/inputs/c1.in;
#  !python3 % < AtCoder/contest322/inputs/c2.in;
#  !python3 % < AtCoder/contest322/inputs/c3.in;

# --- 1. read inputs
n, m = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

# --- 2. DP
res = [0 for _ in range(n+1)]
fireworks = [False for _ in range(n+1)]
for idx in A: fireworks[idx] = True

last = n
for i in range(n, 0, -1):
    if fireworks[i]: last = i
    res[i] = last - i

# --- 3. print res
for r in res[1:]: print(r)
