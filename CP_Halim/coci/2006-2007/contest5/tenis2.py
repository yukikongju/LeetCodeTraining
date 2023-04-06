# Rules:
# (1) A player wins a set if he has 6 or more games and at least two games more than his opponent.
# (2) Additionally, if the result is 6:6 in the first or second set (but not the third set), a single final game is played to determine the winner of the set (the tie-break game).
# (3) The match ends when either player has won 2 sets. That player is the winner.
# (4) federer cannot lose
# (5) winner cannot wins 2-1 if he won the first two sets (TODO)

# Match rules:
# (1) the sets score cannot be: "1:0", "1:1" or "3:0"
# (2) loser is not named federer
# Set rules:
# (3) 

# Valid scores:
# 7-6, 7-5, 6-0, 
# third set: 40-38

# Invalid scores:
#

def read_inputs(file_name):
    with open(file_name, 'r') as f:
        players = f.readline().strip().split()
        n = int(f.readline())
        matchs = [f.readline().strip().split() for _ in range(n) ]
    return players, n, matchs
    
def read_outputs(file_name):
    with open(file_name, 'r') as f:
        ans = f.readlines()
        ans = [ line.strip() for line in ans ]
    return ans
    
def solve(players, n, matchs):
    predictions = []
    for match in matchs:
        # check if match length is valid
        is_valid = True
        if len(match) > 3:
            is_valid = False
            break


        # compute sets each players wins and verify that set are valid
        first, second = 0, 0
        player1_wins, player2_wins = 0, 0
        for i, result in enumerate(match):
            p1, p2 = map(int, result.split(':'))
            tmp = is_set_valid(p1, p2, i+1)
            if not tmp:
                is_valid = False
            else:
                winner = get_set_winner(p1, p2)
                if winner == "p1":
                    player1_wins += 1
                else:
                    player2_wins += 1


        # check if match score is valid: not 1-0, 1-1, 3-0
        if (player1_wins == 3) or (player2_wins == 3): # 3-0
            is_valid = False
        elif (player1_wins == 1 and player2_wins == 0) or (player1_wins == 0 and player2_wins == 1): # 1-0 or 0-1
            is_valid = False
        elif (player1_wins == 1 and player2_wins == 1):
            is_valid = False

        # check if loser is federer
        if is_valid and players[get_loser_idx(player1_wins, player2_wins)] == 'federer':
            is_valid = False



        # get prediction
        prediction = 'da' if is_valid else 'ne'
        predictions.append(prediction)

        # 
        #  print(f"{match} => {is_valid} => P1: {player1_wins} ; P2: {player2_wins} => {prediction}")

    return predictions

def get_loser_idx(p1_wins, p2_wins): # asssume that match is valid
    if p1_wins < p2_wins: # p1
        return 0
    else:
        return 1 # p2
    

def get_set_winner(p1, p2): # assume that set is valid
    if p1 > p2 :
        return "p1"
    else: 
        return "p2"


def is_set_valid(p1, p2, set_num):
    # same score
    if (p1 == p2):
        return False

    # third set
    if (set_num == 3):
        if (max(p1, p2) > 6) and (abs(p1 - p2) == 2):
            return True
        elif (max(p1, p2) == 6) and abs(p1-p2) >= 2:
            return True
        else:
            return False

    # first or second set
    if (p1 == 7) or (p2 == 7):
        if abs(p1-p2) in [1,2]: #7-6 or 7-5
            return True
        else:
            return False
    elif max(p1, p2) == 6: # 6-1, 6-4
        if abs(p1-p2) >=2:
            return True
        else:
            return False
    else: # if max is not 6 or 7
        return False
    

def print_predictions(matchs, predictions, answers):
    for match, ans, pred in zip(matchs, answers, predictions):
        print(f"Match: {match} => Prediction: {pred} ; Answer: {ans}")
    
def print_failed_predictions(matchs, predictions, answers):
    for match, ans, pred in zip(matchs, answers, predictions):
        if ans != pred:
            print(f"Match: {match} => Prediction: {pred} ; Answer: {ans}")
    

def verify_answer(predictions, answers):
    for pred, ans in zip(predictions, answers):
        if pred != ans:
            return 'Failed'
    return 'Passed'
    

def main():
    problem = 'tenis'
    num_problems = 10
    base = f'CP_Halim/coci/2006-2007/contest5/{problem}'
    for i in range(1, num_problems+1):
        input_path = f"{base}/{problem}.in.{i}"
        output_path = f"{base}/{problem}.out.{i}"
        players, n, matchs = read_inputs(input_path)
        answers = read_outputs(output_path)
        predictions = solve(players, n, matchs)
        print('--------------------------------------------------------')
        #  print_predictions(matchs, predictions, answers)
        print_failed_predictions(matchs, predictions, answers)
        #  print(verify_answer(predictions, answers))

    
def test_cases():
    print(f"5-7 : {is_set_valid(5, 7, 2)}") # accept
    print(f"7-5 : {is_set_valid(7, 5, 2)}") # accept
    print(f"7-6 : {is_set_valid(7, 6, 1)}") # accept
    print(f"6-0 : {is_set_valid(6, 0, 1)}") # accept
    print(f"4-2 : {is_set_valid(4, 2, 2)}") # reject
    print(f"2-2 : {is_set_valid(2, 2, 2)}") # reject
    print(f"38-40 : {is_set_valid(38, 40, 3)}") # accept
    print(f"36-40 : {is_set_valid(36, 40, 3)}") # reject
    print(f"6-0 : {is_set_valid(6, 0, 3)}") # accept FIXME; it rejects
    

if __name__ == "__main__":
    main()
    #  test_cases()


