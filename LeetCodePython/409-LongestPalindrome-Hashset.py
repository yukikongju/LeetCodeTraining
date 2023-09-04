#  https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, string: str) -> int:
        # Solution: Hash Set
        # if letter has a pair, we can add it to palindrome
        # at the end, if character still unpaired, we can add it to palindrome in the middle

        longest = 0
        seen = set()
        for s in string:
            if s in seen:
                longest += 2
                seen.remove(s)
            else:
                seen.add(s)
        
        # ---
        if len(seen) > 0:
            longest += 1
        
        # ---
        return longest




        
