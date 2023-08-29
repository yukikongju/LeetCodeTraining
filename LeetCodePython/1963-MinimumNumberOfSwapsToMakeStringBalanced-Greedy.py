#  https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/


class Solution:
    def minSwaps(self, string: str) -> int:
        # solution: Greedy
        # when we have more ] than [, we need to swap ] with the first [ starting at the end
        # explanation: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/solutions/1390811/clear-explanation-c-greedy-detailed-explanation/

        balance, swaps, last = 0, 0, len(string)-1
        string = list(string)

        for i, s in enumerate(string):
            if s == '[':
                balance += 1
            else: # s == ]
                balance -= 1

                if (balance < 0): # swap ] with the first [ starting at the end
                    while (i<last) and (string[last] != '['): last -= 1
                    string[i], string[last] = string[last], string[i]
                    balance = 1
                    swaps += 1
        
        return swaps





