# !python3 % < ICPC/NENA_2023/inputs/L1.in;
# !python3 % < ICPC/NENA_2023/inputs/L2.in;
# solution
# (1) check if max and min have been drank: if not, return max/min
# (2) else print range

# --- 1. read inputs
has_drank_max, has_drank_min = False, False
#  cups = [int(input()) for _ in range(n-1)]
n, a, b = map(int, input().split(' '))

#
for _ in range(n-1):
    cup = int(input())
    if cup == a: has_drank_min = True
    if cup == b: has_drank_max = True

# --- 2. 
if has_drank_min and has_drank_max:
    for i in range(a, b+1): print(i)
elif has_drank_max: print(a)
elif has_drank_min: print(b)
else: print('-1')

