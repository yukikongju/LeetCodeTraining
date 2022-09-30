# submission: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=120&page=show_problem&problem=2267

# Solution 1: 
#       (1) sort dragons heads and knights height
#       (2) check if knight can slay all head


def get_output(problems):
    """ get outputs for all problems """
    outputs = []
    for problem in problems:
        output = get_problem_output(problem)
        outputs.append(output)
    return outputs

def get_problem_output(problem):
    # get problems inputs
    heads = problem.get('heads')
    knights = problem.get('knights')

    heads.sort()
    knights.sort()

    coins = 0
    for knight in knights:
        if heads and heads[0] <= knight:
            coins += knight
            heads.pop()

    if heads: 
        return "Loowater is doomed!"
    else:
        return coins


def read_sample(file_name):
    problems = []
    with open(file_name, 'r') as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())

        while lines:
            line = lines.pop(0)
            if line == "0 0": 
                break
            m, n = line.strip().split(' ')
            heads = []
            knights = []
            for i in range(int(m)):
                line = lines.pop(0)
                heads.append(int(line.strip()))
            for j in range(int(n)):
                line = lines.pop(0)
                knights.append(int(line.strip()))
            problems.append({'heads': heads,'knights': knights})

    return problems


file_name = "CP_Halim/chap1/files/11292_dragon_of_loowater.in"
problems = read_sample(file_name)
outputs = get_output(problems)
print(outputs)
    


