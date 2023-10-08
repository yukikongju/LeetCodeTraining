#  https://atcoder.jp/contests/abc305/tasks/abc305_a

# -- 1. Read inputs
N = int(input())

# -- 2.
delta = 0 if (N % 5) < 3 else 1
borne = (N // 5 + delta)*5
print(borne)

