sample_input1 = """10 4 7"""
sample_input2 = """5 2 2"""
sample_input3 = """4 2 1"""

THICKNESS = 4

def get_largest_piece(n, length, width):
    return max(n-length, length) * max(n-width, width) * THICKNESS


def read_input(sample):
    n, length, width = sample.split(' ')
    return int(n), int(length), int(width)

def main():
    # sample 1
    n, length, width = read_input(sample_input1)
    print(get_largest_piece(n, length, width) == 168)

    # sample 2
    n, length, width = read_input(sample_input2)
    print(get_largest_piece(n, length, width) == 36)

    # sample 3
    n, length, width = read_input(sample_input3)
    print(get_largest_piece(n, length, width) == 24)

if __name__ == "__main__":
    main()
