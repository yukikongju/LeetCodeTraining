#  problem: https://open.kattis.com/contests/n25qzb/problems/robotsonagrid
# solution: DP
import numpy as np

sample1 = """
5
.....
#..#.
#..#.
...#.
.....
"""

sample2 = """ 
7
......#
####...
.#.....
.#...#.
.#.....
.#..###
.#.....
"""

def read_sample(sample):
    lines = sample.strip().split('\n')
    n = int(lines[0])
    grid = []
    for line in lines[1:]:
        grid.append(line)
    return grid, n


def solve(grid, n):
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1

    # fill grid
    for i in range(n):
        for j in range(n):
            if (i==0) and (j==0):
                continue
            if grid[i][j] == '#':
                continue
            # check if up and left sont atteignables
            is_left_attainable = ((j-1 >= 0) and (grid[i][j-1] == '.')) and (dp[i][j-1] != -1)
            is_up_attainable = ((i-1 >= 0) and (grid[i-1][j] == '.')) and (dp[i-1][j] != -1)

            # calculate num of ways
            if is_left_attainable and is_up_attainable: 
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 
            elif is_left_attainable: 
                dp[i][j] = dp[i][j-1] 
            elif is_up_attainable:
                dp[i][j] = dp[i-1][j] 

    print(np.array(dp))

    # return answer
    ans = dp[n-1][n-1]
    if ans == -1:
        return "THE GAME IS A LIE"
    else:
        return ans


#  ------------------------------------------------------------------

def test_sample1(): # sol: 6
    grid, n = read_sample(sample1)
    print(solve(grid, n))


def test_sample2(): # sol: THE GAME IS A LIE
    grid, n = read_sample(sample2)
    print(solve(grid, n))


#  ------------------------------------------------------------------

def main():
    test_sample1()
    test_sample2()
    

if __name__ == "__main__":
    main()
