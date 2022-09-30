#  problem: https://onlinejudge.org/external/103/10360.pdf
#  submission: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=120&page=show_problem&problem=1301

# Solution 1: Brute-Force O(n^2 * m)
#       for each grid cell, calculate the number of rats we can reach and take 
#       the max. from bomb position (x,y) dfs to add the number of rats

# Solution 2: test all position inside convex hull (nlogn * )

# Solution 3: 

# optimisation 1: the grid is too big => resize the grid


import numpy as np

#  GRID_SIZE = 1025
GRID_SIZE = 10

def read_scenarios(file_name):
    with open(file_name, 'r') as f:
        scenarios = []
        num_scenarios = int(f.readline())
        for _ in range(num_scenarios):
            d = int(f.readline())
            num_rat_nest = int(f.readline())
            rat_nests = []
            for _ in range(num_rat_nest):
                #  out = f.readline().replace('\n', '').split(' ')
                x, y, population = f.readline().replace('\n', '').split(' ')
                rat_nests.append([int(x), int(y), int(population)])
            scenarios.append({'d': d, 'nests': rat_nests})
        return scenarios

def get_scenario_output(scenario):
    """ 
    get bomb position (x,y) and num of rats killed with bomb for a given scenarios

    """
    # get scenario input
    d = scenario.get('d')
    nests = scenario.get('nests')

    # initialize grid
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    #  visited = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


    # calculate num of rats reach for all cells
    for x, y, population in nests:
        visited = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        dfs(grid, visited, x, y, population, d)

    # get bomb position and max rats killed
    x_pos, y_pos, max_rats = 0, 0, 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] > max_rats:
                x_pos, y_pos, max_rats = i, j, grid[i][j]

    print(grid)
    #  print(grid[4][4])

    return [x_pos, y_pos, max_rats]
    

def dfs(grid, visited, x, y, population, d): # FIXME: distance
    m, n = len(grid), len(grid[0])
    # check if we are inside the grid
    if (x<0) or (y<0) or (x >= m) or (y >= n) or (visited[x][y]) or (d<0):
        return
    else:
        grid[x][y] += population
        visited[x][y] = True

        dfs(grid, visited, x-1, y, population, d-1)
        dfs(grid, visited, x+1, y, population, d-1)
        dfs(grid, visited, x, y-1, population, d-1)
        dfs(grid, visited, x, y+1, population, d-1)
    

def get_output(scenarios):
    """ 
    get output for all scenarios
    """
    outputs = []
    for scenario in scenarios:
        output = get_scenario_output(scenario)
        outputs.append(output)

    return outputs


file_name = "CP_Halim/chap1/files/10360_rat_attack.in"
scenarios = read_scenarios(file_name)
outputs = get_output(scenarios)
print(outputs)



