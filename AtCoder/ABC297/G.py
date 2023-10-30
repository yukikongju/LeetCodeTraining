#  grundy number explanation: https://codeforces.com/blog/entry/66040

# 1. read inputs
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

# 2. compute nim-sum
grundies = [x % (R+L) for x in A]
nim_sum = 0
for g in grundies:
    nim_sum ^= g // L

# 3. determine if first wins: wins if nim-sum !=0
if nim_sum == 0: print('Second')
else: print('First')

