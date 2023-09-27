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


# --- 2. BFS to find shortest path
#  visited = set()
queue = [(start[0], start[1], '')]
directions = [ (-1, 0, 'U'), (1, 0, 'D'), (0, 1, 'R'), (0, -1, 'L') ]
has_path = [False]


def bfs(i, j, path):
    #  visited.add((i, j))

    # check if we reached end
    if maze[i][j] == 'B':
        print('YES')
        print(len(path))
        print(path)
        has_path[0] = True
        return
    else:
        maze[i][j] = 'X'

        # visited neighbors
        for dx, dy, direction in directions:
            x, y = i+dx, j+dy
            if (x>=0) and (x<m) and (y>=0) and (y<n) and (maze[x][y] in ['.', 'B']):
                queue.append((x, y, path + direction))


# ---
while queue and not has_path[0]:
    i, j, path = queue.pop(0)
    bfs(i, j, path)

# ---
if not has_path[0]:
    print('NO')


