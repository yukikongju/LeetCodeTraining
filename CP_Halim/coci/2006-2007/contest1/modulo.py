"""
Given two integers A and B, A modulo B is the remainder when dividing A by B. For example, the
numbers 7, 14, 27 and 38 become 1, 2, 0 and 2, modulo 3. Write a program that accepts 10 numbers
as input and outputs the number of distinct numbers in the input, if the numbers are considered
modulo 42.
"""

# execute: python3 modulo.py 

def read_input_file(file_name):
    with open(file_name) as f:
        nums = [ int(f.readline().strip()) for _ in range(10) ]
    print(nums)
    return nums
    
def read_output_file(file_name):
    with open(file_name) as f:
        output = int(f.readline().strip())
    return output

def solve(nums):
    s = set()
    for num in nums:
        s.add(num%42)
    return len(s)


#  --------------------------------------------------------------------------

def test_cases():
    num_test_cases = 10
    problem_name = 'modulo'
    base = f"CP_Halim/coci/2006-2007/contest1/{problem_name}"
    for i in range(1, num_test_cases+1):
        in_file = f"{base}/{problem_name}.in.{i}"
        out_file = f"{base}/{problem_name}.out.{i}"
        nums = read_input_file(in_file)
        output = read_output_file(out_file)
        res = solve(nums)
        print(res, output)

def main():
    test_cases()
    

if __name__ == "__main__":
    main()
