# problem: https://cses.fi/problemset/task/1192/
# !python3 % < CSES/GraphAlgorithms/inputs/counting_rooms.in;

# --- 1. Read input
m, n = map(int, input().split(' '))
maze = []
for i in range(m):
    maze.append([cell for cell in input()])

# --- 2. DFS
#  visited = set()
directions = [[1,0], [-1,0], [0,1], [0,-1]]
def dfs(i, j):
    #  visited.add((i, j))
    maze[i][j] = 'X'

    for dx, dy in directions:
        x, y = i+dx, j+dy
        if (x>=0) and (x<m) and (y>=0) and (y<n) and (maze[i][j] == '.'):
            dfs(x,y)

num_rooms = 0
for i in range(m):
    for j in range(n):
        if maze[i][j] == '.':
            dfs(i, j)
            num_rooms += 1

print(num_rooms)
