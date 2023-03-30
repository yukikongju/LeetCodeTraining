#  https://open.kattis.com/problems/minimumscalar
#  solution: sort vector in ascending and descending order and multiply them
#  execute: python3 minimum_scalar.py < scalar/input1.in

def read_inputs():
    n = int(input())
    problems = []
    for _ in range(n):
        length = int(input())
        v1 = [int(num) for num in input().split()]
        v2 = [int(num) for num in input().split()]
        problems.append((v1, v2))
    return n, problems

def solve(n, problems):
    for i in range(n):
        v1, v2 = problems[i]
        v1.sort()
        v2.sort(reverse=True)
        sp = get_scalar_product(v1, v2)

        print(f"Case #{i+1}: {sp}")

def get_scalar_product(v1, v2):
    product = 0
    for s, t in zip(v1, v2):
        product += s*t
    return product

#  --------------------------------------------------------------------------

def main():
    n, problems = read_inputs()
    solve(n, problems)


if __name__ == "__main__":
    main()

