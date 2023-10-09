# https://atcoder.jp/contests/abc306/tasks/abc306_d
# !python3 % < AtCoder/ABC306/inputs/d1.in;

from functools import lru_cache

# --- 1. read inputs
N = int(input())
meals = [tuple(map(int, input().split())) for _ in range(N)]

# --- 2. State: (0) healthy (1) upset (2) dead
dp = {}
def dfs(i, state):
    if (i == N): 
        return 0
    else:
        # if already computed
        if (i, state) in dp:
            return dp[(i, state)]

        # takashi is healthy
        #  if state == 0 and meals[i][1] >= 0:
        if state == 0:
            r1 = dfs(i+1, meals[i][0])
            r2 = dfs(i+1, state)
            taste = max(r2, r1 + meals[i][1])
            dp[(i, state)] = taste
        # takashi is upset
        #  if state == 1 and meals[i][1] >= 0:
        if state == 1:
            next_state = 0 if meals[i][0] == 0 else 2
            if next_state == 0:
                r1 = dfs(i+1, next_state)
                r2 = dfs(i+1, state)
                taste = max(r2, r1 + meals[i][1])
            elif next_state == 2:
                taste = dfs(i+1, state)
            dp[(i, state)] = taste
        #  if state == 2:
        #      return float('-inf')

        return dp[(i, state)]

ans = dfs(0, 0)
#  print(dp)


# --- 3. 
print(ans)

