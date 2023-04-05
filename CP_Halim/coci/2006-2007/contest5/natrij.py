def read_inputs(file_name):
    with open(file_name, 'r') as f:
        start = f.readline().strip()
        end = f.readline().strip()
    return start, end
    
def read_outputs(file_name):
    with open(file_name, 'r') as f:
        ans = f.readline().strip()
    return ans
    
SECONDS_IN_DAY = 24 * 3600

def solve(start, end):
    # 
    s_h, s_m, s_s = map(int, start.split(':'))
    e_h, e_m, e_s = map(int, end.split(':'))

    # count total seconds from start to finish
    s_total = s_h * 3600 + s_m * 60 + s_s
    e_total = e_h * 3600 + e_m * 60 + e_s

    # 
    if e_total > s_total:
        d_total = e_total - s_total
    else:
        d_total = SECONDS_IN_DAY - s_total + e_total

    # format to string
    f_h = str(d_total // 3600)
    f_m = str((d_total % 3600) // 60)
    f_s = str(d_total % 60)
    pad_h = '' if len(f_h) == 2 else '0'
    pad_m = '' if len(f_m) == 2 else '0'
    pad_s = '' if len(f_s) == 2 else '0'
    output = f"{pad_h}{f_h}:{pad_m}{f_m}:{pad_s}{f_s}"

    return output


def main():
    problem = 'natrij'
    num_problems = 10
    base = f'CP_Halim/coci/2006-2007/contest5/{problem}'
    for i in range(1, num_problems+1):
        input_path = f"{base}/{problem}.in.{i}"
        output_path = f"{base}/{problem}.out.{i}"
        start, end = read_inputs(input_path)
        print('--------------------------------------------------------')
        #  print(start, end)
        ans = read_outputs(output_path)
        output = solve(start, end)
        print(f"Test {i} => Output: {output}; Answer: {ans} => {'Passed' if ans == output else 'Failed'}")

    
if __name__ == "__main__":
    main()
