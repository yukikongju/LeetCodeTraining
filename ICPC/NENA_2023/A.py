# !python3 % < ICPC/NENA_2023/inputs/A1.in;
# !python3 % < ICPC/NENA_2023/inputs/A2.in;

from collections import defaultdict

# --- 1. read inputs
n, k, c = map(int, input().split(' '))
teams = [tuple(map(int, input().split(' '))) for _ in range(n)]
schools_counts = defaultdict(int)
winners = []

others = []

# --- 2. (1) get team below count ; if remaining, get higher rank teams
idx = 0
while k and (idx < len(teams)):
    team, school = teams[idx]
    schools_counts[school] += 1

    if schools_counts[school] <= c:
        k -= 1
        winners.append(team)
    else:
        others.append(team)
    idx += 1


idx = 0
while k:
    winners.append(others[idx])
    idx += 1
    k -= 1

# --- 3. print id in orders
winners = set(winners)
for team, _ in teams:
    if team in winners: print(team)

