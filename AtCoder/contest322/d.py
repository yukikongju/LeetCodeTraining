#  https://atcoder.jp/contests/abc322/tasks/abc322_d
# !python3 % < AtCoder/contest322/inputs/d1.in;

# --- 1. read 3 polyomino pieces
N = 4
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]
C = [input() for _ in range(N)]

# --- 2. Brute Force: rotate B and C blocs and test each position

# base case: number of '#' not N*N
num_squares = 0
for row in (A+B+C):
    for cell in row:
        if cell == '#': num_squares += 1

if num_squares != N*N:
    print('No')
    exit()

# 
targets = set()
for i in range(N):
    for j in range(N):
        targets.add((i,j))

def getBlocPositions(X, dx, dy):
    positions = set()
    for i in range(N):
        for j in range(N):
            if X[i][j] == '#': positions.add((i+dx, j+dy))
    return positions

def normalize(S):
    minx = min(S, key=lambda x: x[0])[0]
    miny = min(S, key=lambda x: x[1])[1]
    positions = set((i - minx, j - miny) for i, j in S)
    return positions

def rotate(X):
    #  return list(zip(*X[::-1]))
    return [[X[j][N-i-1] for j in range(N)] for i in range(N)]

# 
ans = False
for rotB in range(N):
    for rotC in range(N):
        for dxB in range(-N+1, N):
            for dyB in range(-N+1, N):
                for dxC in range(-N+1, N):
                    for dyC in range(-N+1, N):
                        setA = getBlocPositions(A, 0, 0)
                        setB = getBlocPositions(B, dxB, dyB)
                        setC = getBlocPositions(C, dxC, dyC)
                        positions = normalize(setA | setB | setC)
                        if positions == targets: ans = True
        C = rotate(C)
    B = rotate(B)


# --- 3.
print('Yes') if ans else print('No')



