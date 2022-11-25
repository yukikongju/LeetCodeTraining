# Solution: count the number of character and calculate permutations
# See: undistinguishable permutations

import math

sample_input1 = """
at
ordeals
abcdefghijklmnopqrstuvwxyz
abcdefghijklmabcdefghijklm
abcdABCDabcd
"""

sample_output1 = """
2
5040
403291461126605635584000000
49229914688306352000000
29937600
"""

#  -------------------------------------------------------------------------


def solve(sample):
    lines = sample.strip().split('\n')
    for line in lines:
        s = line.strip()
        print(get_anagram_count(s))

def get_anagram_count(s):
    # 1. count number of distinct characters
    counts = {}
    for c in s: 
        c = ord(c)
        if c in counts.keys():
            counts[c] += 1
        else: 
            counts[c] = 1

    # 2. count num anagrams
    num_anagrams = math.factorial(len(s))
    for key, value in counts.items():
        num_anagrams //= math.factorial(value)

    return num_anagrams
    
#  -------------------------------------------------------------------------


def main():
    solve(sample_input1)
    

if __name__ == "__main__":
    main()


