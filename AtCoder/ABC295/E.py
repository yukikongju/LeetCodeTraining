#  sol: https://atcoder.jp/contests/abc295/submissions/43715081


from bisect import bisect_left

# 1. read inputs
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353

# --- 2. Compute expected value

# count number of zeroes + sort set values
num_zeroes = 0
B = []
for num in A: 
    if num == 0: num_zeroes += 1
    else:
        B.append(num)
B.sort()
n = len(B)

# 
total = 0
for x in range(1, M+1):
    # TODO: compute probability of getting x at k-th index
    idx = bisect_left(B, x)
    if (idx > K) or (num_zeroes + idx < K):
        px = 0 
        print(x, px)
    else:
        # compute number of zeroes smaller/greater than x
        num_smaller, num_bigger = idx, n-idx
        num_zeroes_smaller, num_zeroes_bigger = K-num_smaller, n-K-num_bigger
        psmaller = num_zeroes_smaller * x/M
        pbigger = num_zeroes_bigger * (M-x)/M
        px = num_zeroes_smaller * psmaller + num_zeroes_bigger * pbigger
        print(x, px, psmaller, pbigger)

    # 
    total += (x * px) % MOD


# --- 3. print values : make expected value integer number


