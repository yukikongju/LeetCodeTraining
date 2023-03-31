#  https://open.kattis.com/problems/firefly
#  execute: python3 firefly.py < firefly/input1.in
#  stalagmites: rising from the floor 
#  stalagtites: hanging from ceiling
# works with sample 2 but not 1
# check if sample 1 has error

def read_inputs():
    n, h = map(int, input().split())
    obstacles = [int(input()) for _ in range(n)]

    return n, h, obstacles

def print_cave(n, h, stalagmites, stalagtites):
    pass
    

def get_stalagmites_stalagtites(obstacles):
    stalagmites, stalagtites = [], []
    for i, obs in enumerate(obstacles):
        if i % 2 == 0:
            stalagmites.append(obs)
        else:
            stalagtites.append(obs)
    return stalagmites, stalagtites

def get_obstacles_count(n, h, stalagmites, stalagtites):
    # 1. count stalagmites and stalagtites ending at level
    stalagmite_count = get_dict_count(stalagmites)
    stalagtite_count = get_dict_count(stalagtites)

    # 2. count stalagmites and stalagtites at each level with running sum
    running_sum = 0
    stalagtites_level = {}
    for level in range(1, h+1):
        running_sum += stalagtite_count.get(level, 0)
        stalagtites_level[level] = running_sum

    running_sum = 0
    stalagmites_level = {}
    for level in reversed(range(1, h+1)):
        running_sum += stalagmite_count.get(level, 0)
        stalagmites_level[level] = running_sum

    print(stalagmites_level, stalagtites_level)

    # 3. count obstacles at each level
    level_obstacles, obstacles_count = {}, {}
    min_obstacles = float('inf')
    for level in range(1, h+1):
        # 
        level_obstacles[level] = num_obstacles = stalagmites_level[level] + stalagtites_level[level]
        min_obstacles = min(min_obstacles, num_obstacles)

        #
        obstacles_count[num_obstacles] = obstacles_count.get(num_obstacles, [])
        obstacles_count[num_obstacles].append(level)

    print(min_obstacles)
    print(level_obstacles)
    print(obstacles_count)

    # 4. return values: min obstacles, num level with min obstacles
    num_levels = len(obstacles_count[min_obstacles])

    return min_obstacles, num_levels

    
def get_dict_count(array):
    counts = {}
    for item in array:
        counts[item] = counts.get(item, 0) + 1
    return counts

#  --------------------------------------------------------------------------


def main():
    n, h, obstacles = read_inputs()
    stalagmites, stalagtites = get_stalagmites_stalagtites(obstacles)
    print(stalagmites, stalagtites)
    min_obstacles, num_levels = get_obstacles_count(n, h, stalagmites, stalagtites)
    print(min_obstacles, num_levels)

if __name__ == "__main__":
    main()

