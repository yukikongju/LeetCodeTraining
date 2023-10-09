#  https://atcoder.jp/contests/abc305/tasks/abc305_c
# !python3 % < AtCoder/ABC305/inputs/c1.in;

# --- 1. read inputs
H, W = map(int, input().split())
grid = [[ c for c in input() ] for _ in range(H)]

# --- 2.

# 
start_row, end_row, start_col, end_col = H, 0, W, 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            start_row = min(start_row, i)
            end_row = max(end_row, i)
            start_col = min(start_col, j)
            end_col = max(end_col, j)

#  print(start_row, end_row, start_col, end_col)

# 
for i in range(start_row, end_row+1):
    for j in range(start_col, end_col+1):
        if grid[i][j] != '#':
            res = (i+1, j+1)
            break

# --- 3. 
print(' '.join(map(str, res)))

