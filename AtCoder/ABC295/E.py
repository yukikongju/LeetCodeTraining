#  sol: https://atcoder.jp/contests/abc295/submissions/43715081

from bisect import bisect_left

# 1. read inputs
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
M_inv = pow(M, mod-2, mod) # inverse modulo

# count number of zeroes + sort set values
num_zeroes = A.count(0)
B = sorted(A)
non_zeroes = N - num_zeroes

# --- 2. Compute expected value

# precompute factorial and inverse factorial to compute binomial coefficients
factorial = [1]
inverse = [1]
for i in range(1, N+1):
    factorial.append(factorial[-1]*i%mod)
    inverse.append(pow(factorial[-1], mod-2, mod))

def binomial(N, R, mod):
    if N < R or R < 0:
        return 0
    elif R == 0 or R == N:
        return 1
    else:
        return factorial[N] * inverse[R] * inverse[N-R] % mod


# compute probability of getting x at k-th index
total = 0
for m in range(1, M+1):
    s = N - bisect_left(B, m)
    required = max(N-K+1-s, 0)
    for t in range(required, num_zeroes+1):
        alpha = pow((M-m+1)*M_inv, t, mod) # probability that at least t elements >= x
        beta = pow((m-1)*M_inv, num_zeroes-t, mod) # probability that at most num_zeroes-t elements < x
        gamma = alpha * beta % mod
        total += binomial(num_zeroes, t, mod) * gamma
    total %= mod

# --- 3. print values : make expected value integer number
print(total)

