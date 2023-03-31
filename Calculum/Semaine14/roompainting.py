#  https://open.kattis.com/problems/roompainting
#  exectute: python3 roompainting.py < roompaintings/input.in
#  solution 1: naive O(n*m)
#  solution 2: greedy + binary search: O(m*log n)
#  CHECK


def read_inputs():
    n, m = map(int, input().split())
    sizes = [int(input()) for _ in range(n)]
    colors = [int(input()) for _ in range(m)]
    return n, m, sizes, colors


def can_fill(color, can_size):
    return color <= can_size

def get_waste(n, m, sizes, colors):
    waste = 0
    for color in colors:
        idx = get_container_index(color, sizes)
        container_size = sizes[idx] if idx<n else sizes[-1]
        waste += container_size - color if can_fill(color, container_size) else 0
    return waste
    
def get_container_index(x, values):
    low, high = 0, len(values)
    while low < high: 
        mid = (low + high)//2
        if x > values[mid]:
            low = mid + 1
        else:
            high = mid
    return low
    
#  --------------------------------------------------------------------------

def main():
    n, m, sizes, colors = read_inputs()
    #  print(n, m, sizes, colors)
    waste = get_waste(n, m, sizes, colors)
    print(waste)

if __name__ == "__main__":
    main()
