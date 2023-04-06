# 5:7 third set
# same number of sets wons


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
        first, second = 0, 0
        is_valid = True
        for i, result in enumerate(match):
            # check if length is valid
            if (len(match) == 1) or (len(match) > 2):
                is_valid = False
                break

            tmp = is_set_valid(result, i+1)
            #  print(result, tmp)
            if not tmp:
                is_valid = False

        prediction = 'da' if is_valid else 'ne'
        predictions.append(prediction)

    return predictions

def is_set_valid(result, set_num):
    p1 , p2 = map(int, result.split(':'))
    if (p1 == p2):
        return False
    elif (p1 == 7) or (p2 == 7):
        if (abs(p1 - p2) > 2) or (set_num > 2) or (p1 - p2 == 0): 
            return False
        else: 
            return True
    elif (p1 == 6) or (p2 == 6): 
        if abs(p1 - p2) < 2:
            return False
        else:
            return True
    else: 
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
    print(is_set_valid('5:7', 2))
    print(is_set_valid('7:5', 2))
    print(is_set_valid('4:2', 2))
    print(is_set_valid('2:2', 2))
    

if __name__ == "__main__":
    #  main()
    test_cases()

