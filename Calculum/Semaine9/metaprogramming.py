
test_sample1 = """
define 5 hellothere
define 6 goodbye
eval hellothere < goodbye
eval hellothere > goodbye
eval hellothere = goodbye
eval hellothere = hi
define 5 hi
eval hellothere = hi
define 6 hi
eval hellothere = hi
"""


#  -------------------------------------------------------------------------

def solve(sample):
    lines = sample.split('\n')
    word_dict = {}
    for line in lines:
        words = line.split(' ')
        if words[0] == 'define':
            word_dict[words[2]] = int(words[1])
        elif words[0] == 'eval':
            if words[1] not in word_dict.keys() and words[3] not in word_dict.keys():
                print('undefined')
            else:
                symbol = words[2]
                val1, val2 = word_dict.get(words[1]), word_dict.get(words[3])
                if symbol == '<':
                    print(val1 < val2)
                elif symbol == '>':
                    print(val1 > val2)
                else: # =
                    print(val1 == val2)
    


#  -------------------------------------------------------------------------


def main():
    solve(test_sample1)
    

if __name__ == "__main__":
    main()
