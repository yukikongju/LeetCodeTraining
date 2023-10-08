# https://atcoder.jp/contests/abc322/tasks/abc322_e
# !python3 % < AtCoder/contest322/inputs/e1.in;

from functools import lru_cache

# --- 1. Read inputs
N, K, P = map(int, input().split())
C, A = [], []
for _ in range(N):
    row = list(map(int, input().split()))
    C.append(row[0])
    A.append(row[1:])

# --- 2. Backtracking/DFS + Memoization using LRU cache

@lru_cache(maxsize=None)
def backtracking(i, params):
    if (i == N):
        return 0 if all(x >= P for x in params) else float('inf')
    else:
        # don't do the plan
        res1 = backtracking(i+1, params)

        # do the plan
        params2 = tuple(min(P, params[j] + A[i][j]) for j in range(K))
        res2 = backtracking(i+1, params2)

        # best cost
        res = min(res1, C[i] + res2)
        return res

ans = backtracking(0, (0,)*K)


# --- 3. print answers
print(ans) if ans < float('inf') else print('-1')

