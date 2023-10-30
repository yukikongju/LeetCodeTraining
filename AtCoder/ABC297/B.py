# 1. read inputs
S = input()

k = S.index('K')
q = S.index('Q')
b1 = S.index('B')
b2 = S.rindex('B')
r1 = S.index('R')
r2 = S.rindex('R')

has_same_parities = (b1 % 2 == b2 % 2)
is_k_between_r = (r1 < k < r2)

if (not has_same_parities) and (is_k_between_r):
    print('Yes')
else:
    print('No')
