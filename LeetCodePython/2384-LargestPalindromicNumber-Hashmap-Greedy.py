#  https://leetcode.com/problems/largest-palindromic-number/description/

class Solution:
    def largestPalindromic(self, num: str) -> str:
        # solution: hashmap + Greedy
        # we can only use '0' if there is at least 2 digits

        # --- count dict
        count_dict = defaultdict(int)
        for n in num: 
            count_dict[n] += 1

        # --- build first half of palindrome
        stack = []
        for i in range(9, 0, -1):
            s = str(i)
            while count_dict[s] >= 2:
                stack.append(s)
                count_dict[s] -= 2

        # ---- use zeros only if half is not empty
        if len(stack) > 0:
            while count_dict['0'] >= 2:
                count_dict['0'] -= 2
                stack.append('0')

        # --- use largest remaining number as center digit
        largest_remaining_digit = ''
        for i in range(9, -1, -1):
            s = str(i)
            if count_dict[s] >= 1:
                largest_remaining_digit = s
                break

        # --- build largest palindromic integer
        output = stack + [largest_remaining_digit] + stack[::-1]
        return ''.join(output)
        
