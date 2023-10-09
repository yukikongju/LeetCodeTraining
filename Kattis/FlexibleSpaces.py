#  https://open.kattis.com/problems/flexible
# !python3 % < Kattis/inputs/flexible_spaces1.in;

# --- 1. read inputs
W, P = map(int, input().split())
L = list(map(int, input().split()))
L = L + [W]

# --- 2. 
sols = set(L)
for i in range(len(L)):
    for j in range(i+1, len(L)):
        #  print(i, j)
        l = L[j] - L[i]
        sols.add(l)


# --- 3. 
sols = list(sols)
sols.sort()
print(*sols)

