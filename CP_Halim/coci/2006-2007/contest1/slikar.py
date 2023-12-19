# Graph Problem:
#  Solution: BFS + shortest path
#  (1) calculate time to flood each . from each *
#  (2) calculate distance from S to D (avoid flood?)
#  FIXME: doesn't work with test case 4,9 => Need to take flood into account

import numpy as np
import copy 


def read_input_file(file_name):
    with open(file_name) as f:
        r, c = map(int, f.readline().strip().split())
        forest = [[s for s in f.readline().strip()] for _ in range(r) ]
    return r, c, forest
    
def read_output_file(file_name):
    with open(file_name) as f:
        ans = f.readline().strip()
    return ans

def print_grid(grid):
    pass

    

def solve(r, c, forest):

    grid = copy.deepcopy(forest)
    distances = copy.deepcopy(forest)

    # 1. find position of D, S and floods
    floods = []
    for i, row in enumerate(forest):
        for j, cell in enumerate(row):
            if cell == 'D':
                destination = (i, j)
            elif cell == 'S':
                source = (i, j)
            elif cell == '*':
                floods.append((i, j))

    # 2. Find time to flood all cells with BFS
    time = 0
    while floods:
        time += 1
        for _ in range(len(floods)):
            i, j = floods.pop(0)

            # bfs
            directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for row, col in directions:
                if (row >= 0) and (col >=0) and (row < r) and (col < c) and (forest[row][col] in ['.', 'D']):
                    forest[row][col] = time
                    floods.append((row, col))

    # 3. Compute time to reach each cell with BFS
    positions = [source]
    time = 0
    while positions:
        time += 1
        for _ in range(len(positions)):
            i, j = positions.pop(0)

            # bfs
            directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for row, col in directions:
                if (row >= 0) and (col >=0) and (row < r) and (col < c) and (distances[row][col] in ['.', 'D']): # FIXME
                    distances[row][col] = time
                    positions.append((row, col))

    # print grid
    print(np.array(grid))
    print('-----------')
    print(np.array(forest))
    print('-----------')
    print(np.array(distances))


    # 4. check if wizard can reach
    d_distance = distances[destination[0]][destination[1]]
    d_flood = forest[destination[0]][destination[1]]
    if (d_distance == 'D'):
        return 'KAKTUS'
    elif (d_distance != 'D') and (d_flood == 'D'):
        return d_distance
    elif (int(d_flood) < int(d_distance)):
        return 'KAKTUS'
    else:
        return d_distance


#  --------------------------------------------------------------------------

def test_cases():
    num_test_cases = 4
    problem_name = 'slikar'
    base = f"CP_Halim/coci/2006-2007/contest1/{problem_name}"
    for i in range(4, num_test_cases+1):
        in_file = f"{base}/{problem_name}.in.{i}"
        out_file = f"{base}/{problem_name}.out.{i}"
        r, c, forest = read_input_file(in_file)
        ans = read_output_file(out_file)
        output = solve(r, c, forest)
        print(f"Test case {i} => Output: {output} ; Answer: {ans} => {'Passed' if (ans == str(output)) else 'Failed'}")

def main():
    test_cases()
    

if __name__ == "__main__":
    main()
