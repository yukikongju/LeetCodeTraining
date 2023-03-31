#  Solution:

def read_input_file(file_name):
    with open(file_name) as f:
        string = f.readline().strip()
    return string
    
def read_output_file(file_name):
    with open(file_name) as f:
        output = [f.readline().strip() for _ in range(5)]
    return output

def solve(letters): 
    n = len(letters)
    m = 5*n - (n-1)

    # generate 1rst line
    first = ""
    i = 0
    while len(first) < m-4:
        i += 1
        if i % 3 == 0:
            first += '..*.'
        else: 
            first += '..#.'
    first += '.'

    # generate 2nd line
    second = ""
    i = 0
    while len(second) < m-2:
        i += 1
        if (i % 6 == 5) or (i%6==0):
            second += '.*'
        else:
            second += '.#'
    second += '.'

    # generate 3rd line
    third = "#"
    i = 0
    while len(third) < m - 2:
        if (i%3 ==0):
            third +=  '.' + letters[i] + '.#'
        else: 
            third +=  '.' + letters[i] + '.*'
        i += 1
    
    # replace character if second to last is #
    if i % 3 != 0:
        third = third[:-1] + '#'

    ans = [first, second, third, second, first]
    return ans


def print_output(output):
    for line in output:
        for c in line:
            print(c, end='')
        print('\n')
    
def check_ans(ans, output):
    is_first_correct = ans[0] == output[0]
    is_second_correct = ans[1] == output[1]
    is_third_correct = ans[2] == output[2]
    print(f"First: {is_first_correct} => Second: {is_second_correct} => Third: {is_third_correct}")

    if not is_first_correct:
        print(ans[0])
        print(output[0])
    if not is_second_correct:
        print(ans[1])
        print(output[1])
    if not is_third_correct:
        print(ans[2])
        print(output[2])



#  --------------------------------------------------------------------------

def test_cases():
    num_test_cases = 10
    problem_name = 'okviri'
    base = f"CP_Halim/coci/2006-2007/contest1/{problem_name}"
    for i in range(1, num_test_cases+1):
        in_file = f"{base}/{problem_name}.in.{i}"
        out_file = f"{base}/{problem_name}.out.{i}"
        string = read_input_file(in_file)
        output = read_output_file(out_file)
        print('-------------')
        ans = solve(string)
        print(f"Test #{i}: {len(string)} => {'Passed' if ans == output else 'Failed'}")
        check_ans(ans, output)
        print('-------------')

def main():
    test_cases()
    

if __name__ == "__main__":
    main()

