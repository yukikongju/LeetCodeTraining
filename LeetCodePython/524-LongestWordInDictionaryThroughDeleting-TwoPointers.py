#  https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # solution: two pointers

        # - 
        def find(s, word) -> bool:
            i, j = 0, 0
            while (i < len(s)) and (j < len(word)):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return True if j == len(word) else False
        
        longest = ""
        for word in dictionary:
            is_complete = find(s, word)
            if is_complete and len(word) > len(longest):
                longest = word
            elif is_complete and len(word) == len(longest):
                longest = min(word, longest)

        return longest
            
