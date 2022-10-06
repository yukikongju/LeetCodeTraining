#  Problem: https://onlinejudge.org/external/114/11450.pdf

# Solution 1: Générer toutes les combinaisons et prendre le max inférieur (DFS)
# Solution 2: 

import numpy as np


def solve(problems):
    for problem in problems:
        output = solve_problem(problem)
        print(output)


def solve_problem(problem):
    # Solution: backtracking
    money = int(problem.get('money'))
    num_garments = problem.get('k')
    garments = problem.get('garments')

    # convert list string to int
    num_garments = [int(i) for i in num_garments]
    garments = [[int(garments[i][j]) for j in range(len(garments[i]))] for i in range(len(garments))]

    print(money)
    print(num_garments)
    print(garments)
    # 1. price of garnments when we buy it k times
    #  for i, (k, garment) in enumerate(zip(num_garments, garments)):
    #      for j in range(len(garments[i])):
    #          pass


    # find solutions
    solutions = []
    backtrack(solutions, [], num_garments, garments, money)

    # find best solution
    max_cost = 0
    best_garment = []
    for solution in solutions:
        cost = 0
        for i, garment_cost in enumerate(solution):
            cost += num_garments[i] * garment_cost
        if cost > max_cost: 
            max_cost = cost
            best_garment = solution

    print(max_cost, best_garment)

    return solutions

    
def backtrack(solutions, v, k, garnments, budget):
    """ 
    construire vecteur c-prometteur

    Parameters
    ----------
    v: list
        vecteur prometteur. Liste des items choisis
    k: list
        nombre d'items à selectionner parmis le i-e garnments
    garnments: list of list
        cout unitaire des items d'un garnment
    budget: int
        budget restant pour acheter le reste des garnments
    """
    if len(v) == len(garnments):
        solutions.append(v)
    else: 
        idx = len(v)
        for cout_unitaire in garnments[idx]:
            cout = k[idx] * cout_unitaire
            if budget - cout >= 0:
                w = v + [cout_unitaire]
                backtrack(solutions, w, k, garnments, budget-cout)



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

