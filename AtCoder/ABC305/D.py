# https://atcoder.jp/contests/abc305/submissions/46397615
# !python3 % < AtCoder/ABC305/inputs/d1.in;

import bisect

# --- 1. read inputs
N = int(input())
A = list(map(int, input().split()))
Q = int(input())


# --- 2. Build Prefix Sum [S] + Binary search to find intervals
S = [0 for _ in range((N+1)//2)]
for i in range((N - 1) // 2):
    S[i+1] = A[2*i+2] - A[2*i+1] + S[i]
#  print(S)

res = []
for _ in range(Q):
    l, r = map(int, input().split())
    lp = bisect.bisect_right(A, l)
    rp = bisect.bisect_left(A, r)

    # if not multiple of 2, add interval
    if (lp == rp) and (lp&1==0):
        duration = r - l
    else:
        li = A[lp] - l if (lp&1==0) else 0
        ri = r - A[rp-1] if (rp&1==0) else 0
        duration = S[(rp-1)//2] - S[lp//2] + li + ri

    res.append(duration)

# --- 3. print answers
for r in res: print(r)

