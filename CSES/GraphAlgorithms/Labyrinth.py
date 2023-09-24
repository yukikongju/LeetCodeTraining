#  https://cses.fi/problemset/task/1193
# !python3 % < CSES/GraphAlgorithms/inputs/labyrinth.in;

# --- 1. Read Inputs + find start (A) and end (B)
m, n = map(int, input().split(' '))
maze = [['' for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j, cell in enumerate(input()):
        maze[i][j] = cell
        if cell == 'A': start = (i, j)
        if cell == 'B': end = (i, j)

#  print(m, n)
#  print(maze)
#  print(start, end)

# --- 2. BFS to find shortest path
queue = [(start[0], start[1], '')]
visited = set()
directions = [ (-1, 0, 'U'), (1, 0, 'D'), (0, 1, 'R'), (0, -1, 'L') ]
has_path = False


def bfs(i, j, path):
    visited.add((i, j))

    #  print(i, j, path)

    # check if we reached end
    if maze[i][j] == 'B':
        print('YES')
        print(len(path))
        print(path)
        has_path = True

    # visited neighbors
    for dx, dy, direction in directions:
        x, y = i+dx, j+dy
        if (x>=0) and (x<m) and (y>=0) and (y<n) and (maze[x][y] in ['.', 'B']) and ((x, y) not in visited):
            queue.append((x, y, path + direction))



# ---
while queue:
    i, j, path = queue.pop(0)
    #  print(i, j, path)
    bfs(i, j, path)

# ---
if not has_path:
    print('NO')


