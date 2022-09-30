# SOLUTION: DFS
# optim1: 3 cases => on split le problème en 2

# Solution 1: Brute-Force
# Explanation: https://www.youtube.com/watch?v=vYPwYz-rAmM
#       We try every subproblems: we can move if 
#           (1) board[i] == 'o'
#           (2) board[i+1] == 'o'
#           (3) board[i+2] == '-'
#       We can use a hashmap to store computed values

# Solution 2: 

import os


def brute_force(pebbles):
    """
    We calculate every subproblems
    """
    # calculate the number of pebbles
    min_counts = [0]*len(pebbles)
    hashmap = {}
    for i, board in enumerate(pebbles):
        min_count = helper(list(board), hashmap)
        #  min_counts[i] = str(min_count)
        min_counts[i] = min_count

    return min_counts
    

def helper(board, hashmap):
    """ 
    Calculate minimum of pebbles in a given row
    """
    print(''.join(board))
    # check if board has been computed
    board_str = ''.join(board)
    if board_str in hashmap: 
        return hashmap.get(board_str)

    # calculate the number of pebbles originally
    count = 0
    for symbol in board:
        if symbol == 'o':
            count += 1

    # find subproblems from left to right
    m = len(board)
    for i, symbol in enumerate(board[:m-2]):
        # try to move pebble: next slot is pebble and next is empty
        if (symbol == 'o') and (board[i+1] == 'o') and (board[i+2] == '-'):
            new_board = board
            new_board[i] = '-'
            new_board[i+1] = '-'
            new_board[i+2] = 'o'
            new_value = helper(new_board, hashmap)
            if new_value < count:
                count = new_value

    # find subproblems from right to left
    for i, symbol in enumerate(board[2:m]):
        if (symbol == 'o') and (board[i-1] == 'o') and (board[i-2] == '-'):
            new_board = board
            new_board[i] = '-'
            new_board[i-1] = '-'
            new_board[i-2] = 'o'
            new_value = helper(new_board, hashmap)
            if new_value < count:
                count = new_value

    hashmap[board_str] = count

    return count


def read_input(file_name):
    with open(file_name) as f:
        n = f.readline().strip()
        pebbles = []
        for line in f.readlines():
            pebbles.append(line.strip())

        return n, pebbles


def main():
    file_name = "Calculum/Semaine2/pebblesolitaire/pebblesolitaire.in"
    n, pebbles = read_input(file_name)

    # Solution 1:
    #  min_counts = brute_force(pebbles)
    #  print(min_counts)
    #  print(' '.join(min_counts))

    # test edge case 
    board = 'oooooooooo-o'
    print(helper(list(board), {}))


if __name__ == "__main__":
    main()
