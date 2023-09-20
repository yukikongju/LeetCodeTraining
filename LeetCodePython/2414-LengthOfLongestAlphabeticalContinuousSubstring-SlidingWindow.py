#  https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/description/

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # solution: sliding window

        # --- 
        pointer = 0
        max_length = 1
        for i in range(1, len(s)):
            letter, prev_letter = s[i], s[i-1]
            if ord(prev_letter) + 1 != ord(letter):
                pointer = i
            max_length = max(max_length, i-pointer+1)
        return max_length
