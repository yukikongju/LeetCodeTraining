# https://atcoder.jp/contests/abc306/tasks/abc306_d
# !python3 % < AtCoder/ABC306/inputs/d1.in;

# --- 1. read inputs
N = int(input())

# --- 2. State: (0) healthy (1) upset // (2) dead; [0] dont eat ; [1] eat
dp = [[float('-inf') for _ in range(2)] for _ in range(N+1)]
dp[0][0] = 0
dp[0][1] = float('-inf')

for i in range(N):
    x, y = map(int, input().split())
    if x == 0: # antidote
        dp[i+1][0] = max(dp[i][0], dp[i][1]+y, dp[i][0]+y)
        dp[i+1][1] = dp[i][1]
    if x == 1: # poison
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = max(dp[i][1], dp[i][0] + y)

# --- 3.
print(max(dp[N]))
