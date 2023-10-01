# !python3 % < ICPC/NENA_2023/inputs/G.in;

# --- 1. read inputs
n, lph = map(int, input().split(' '))
problems = [int(input()) for _ in range(n)]
MAX_TIME = 5.0

# --- 2. Run greedy algorithm
problems.sort()

max_problems = 0
time = 0
for problem in problems:
    time += problem / lph
    if time <= MAX_TIME:
        max_problems += 1
    else:
        break

print(max_problems)

