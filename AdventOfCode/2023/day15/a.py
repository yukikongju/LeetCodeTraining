from functools import reduce


def run_hash_algo(s: str):
    return reduce(lambda res, c: (res + ord(c)) * 17 % 256, s, 0)

def run_hash_algo2(s: str):
    res = 0
    for c in s:
        res = (res + ord(c)) * 17 % 256
        #  res = (res + ord(c)) * 17 & 0xFF
    print(res)
    return res

def read_inputs(file_name: str):
    with open(file_name, "r") as f:
        res = f.readline().strip().split(',')
    return res


def part1():
    #  FILE_NAME = "~/Projects/LeetCodeTraining/AdventOfCode/2023/day15/inputs/1.txt"
    FILE_NAME = "inputs/1.txt"
    inputs = read_inputs(file_name=FILE_NAME)

    # --- PART 1
    res = sum([run_hash_algo2(s) for s in inputs])
    print(res)



if __name__ == "__main__":
    part1()

    
