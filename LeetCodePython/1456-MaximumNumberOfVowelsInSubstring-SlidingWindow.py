#  https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # solution: sliding window

        # --- check if letter is vowels
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        dp = [1 if letter in vowels else 0 for letter in s]
        count = sum(dp[:k])
        n = len(s)

        # --- sliding window
        max_vowels = count
        for i in range(k, n):
            last_letter = dp[i-k]
            next_letter = dp[i]
            count = count - last_letter + next_letter
            max_vowels = max(max_vowels, count)
    
        return max_vowels
        
