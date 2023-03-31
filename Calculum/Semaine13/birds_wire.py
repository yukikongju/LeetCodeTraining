#  https://open.kattis.com/problems/birds
#  execute: python3 birds_wire.py < birds/input1.in
#  solution: O(nlogn * n)
#  (1) sort array in ascending order
#  (2) compute num of birds we can insert between each intervals with floor
#  DOESNT PASS ALL TEST


def read_inputs():
    l, d, n= map(int, input().split())
    positions = []
    for _ in range(n):
        positions.append(int(input()))
    return l, d, n, positions

def solve(l, d, n, positions):
    if n == 0:
        return (l-12)//d + 1

    # sort
    positions.sort()
    right_border = l - 6

    # count number of birds in each intervals
    total = 0
    current = 6
    for position in positions:
        while (position - current >= d):
            current += d
            total += 1
        current += d

    while current < (l-6):
        current += d
        total += 1

    return total


#  -------------------------------------------------------------------------


def main():
    l, d, n, positions = read_inputs()
    ans = solve(l, d, n, positions)
    print(ans)
    
if __name__ == "__main__":
    main()

