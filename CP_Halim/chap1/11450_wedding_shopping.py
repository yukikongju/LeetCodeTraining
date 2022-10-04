# Solution 1: Générer toutes les combinaisons et prendre le max inférieur (DFS)

def solve(problems):
    for problem in problems:
        output = solve_problem(problem)


def solve_problem(problem):
    # Solution: backtracking
    money = problem.get('money')
    num_garments = problem.get('k')
    garments = problem.get('garments')

    # 1. price of garnments when we buy it k times
    for i, k, garment in enumerate(zip(num_garments, garments)):
        for j in range(len(garments[i])):
            pass


    print(money)
    print(num_garments)
    print(garments)
    
def helper():
    pass
    



def read_sample(file_name):
    problems = []
    with open(file_name) as f:
        num_tests = int(f.readline().strip())
        for _ in range(num_tests):
            money, num_garments = f.readline().strip().split(' ')
            problem_garnments = []
            ks = []
            for _ in range(int(num_garments)):
                garnment = f.readline().strip().split(' ')
                k = garnment[0]
                ks.append(k)
                garnments = garnment[1:]
                problem_garnments.append(garnments)
            problems.append({'money': money, 'k': ks, 'garments': problem_garnments})
    return problems

def main():
    file_name = "CP_Halim/chap1/files/11450_wedding_shopping.in"
    problems = read_sample(file_name)
    solve_problem(problems[0])


if __name__ == "__main__":
    main()

