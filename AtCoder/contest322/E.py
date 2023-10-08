# https://atcoder.jp/contests/abc322/tasks/abc322_e
# !python3 % < AtCoder/contest322/inputs/e1.in;

#  from functools import lru_cache

# --- 1. read inputs
N, K, P = map(int, input().split())
C, A = [], []
for _ in range(N):
    row = list(map(int, input().split()))
    C.append(row[0])
    A.append(row[1:])

# --- 2. Backtracking with LRU cache

dp = {}
def backtracking(i: int, params: tuple):
    if i == N:
        return 0 if all(x >= P for x in params) else float('inf')
    else:
        if (i, params) in dp:
            return dp[(i, params)]

        # don't do the plan
        res1 = backtracking(i+1, params)

        # do the plan
        params2 = tuple(params[j] + A[i][j] for j in range(K))
        res2 = backtracking(i+1, params2)

        # select best cost
        res = min(res1, C[i] + res2)
        dp[(i, params)] = res

        return res

ans = backtracking(0, tuple([0]*K))

# --- 3. print ans
print(ans) if ans < float('inf') else print('-1')

