#  taxicab: square inside circle: 2*r**2
#  euclidean: pi*r**2

import math

def read_input_file(file_name):
    with open(file_name) as f:
        n = int(f.readline().strip())
    return n
    
def read_output_file(file_name):
    with open(file_name) as f:
        euclidean = float(f.readline())
        taxicab = float(f.readline())
    return euclidean, taxicab

def solve(n):
    taxicab = 2*n**2
    euclidean = math.pi*n**2
    return euclidean, taxicab


#  --------------------------------------------------------------------------

def test_cases():
    num_test_cases = 10
    problem_name = 'herman'
    base = f"CP_Halim/coci/2006-2007/contest1/{problem_name}"
    for i in range(1, num_test_cases+1):
        in_file = f"{base}/{problem_name}.in.{i}"
        out_file = f"{base}/{problem_name}.out.{i}"
        n = read_input_file(in_file)
        euclidean, taxicab = read_output_file(out_file)
        res_euc, res_taxi = solve(n)
        print(f"[Euclidean] => predicted: {res_euc} => true: {euclidean}")
        print(f"[Taxicab] => predicted: {res_taxi} => true: {taxicab}")

def main():
    test_cases()
    

if __name__ == "__main__":
    main()
