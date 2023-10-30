# !python3 A.py < "AtCoder/ABC297/inputs/a/1.in"
# python3 A.py < inputs/a/1.in

# 1. read inputs

N, D = map(int, input().split())
clicks = [int(t) for t in input().split()]

for i in range(len(clicks)-1):
    diff = clicks[i+1] - clicks[i]
    if diff <= D:
        print(clicks[i+1])
        exit(0)

print('-1')
