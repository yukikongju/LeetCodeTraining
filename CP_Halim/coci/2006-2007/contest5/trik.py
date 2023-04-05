
def read_inputs(file_name):
    with open(file_name, 'r') as f:
        s = f.readline().strip()
    return s
    
def read_outputs(file_name):
    with open(file_name, 'r') as f:
        ans = int(f.readline().strip())
    return ans
    
def solve(s):
    pos = 1
    for move in s:
        if move == 'A':
            if pos == 1:
                pos = 2
            elif pos == 2:
                pos = 1
        elif move == 'B':
            if pos == 2:
                pos = 3
            elif pos == 3:
                pos = 2
        elif move == 'C':
            if pos == 1:
                pos = 3
            elif pos == 3:
                pos = 1
    return pos


def main():
    problem = 'trik'
    num_problems = 5
    base = f'CP_Halim/coci/2006-2007/contest5/{problem}'
    for i in range(1, num_problems+1):
        input_path = f"{base}/{problem}.in.{i}"
        output_path = f"{base}/{problem}.out.{i}"
        s = read_inputs(input_path)
        ans = read_outputs(output_path)
        output = solve(s)
        print(f"Test {i} => Output: {output}; Answer: {ans} => {'Passed' if ans == output else 'Failed'}")

    
if __name__ == "__main__":
    main()
