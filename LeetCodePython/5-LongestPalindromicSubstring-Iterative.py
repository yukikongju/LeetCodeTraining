#  https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # consider each letter as the center and expand from there
        longest = ""
        max_length = 0
        
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while (l >=0) and (r <len(s)) and s[l] == s[r]:
                if (r-l+1) > max_length:
                    longest = s[l:r+1]
                    max_length = len(longest)
                l -= 1
                r += 1
            
            # even length
            l, r = i, i+1
            while (l >= 0) and (r <len(s)) and s[l] == s[r]:
                if (r-l+1) > max_length:
                    longest = s[l:r+1]
                    max_length = len(longest)
                l -= 1 
                r += 1
        
        return longest
        
                    
                
            
