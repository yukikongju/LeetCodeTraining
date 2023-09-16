#  https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, string: str) -> str:
        # 

        # --- get word list without trailing spaces
        words = []
        current = ""
        for s in string:
            if s != ' ':
                current += s
            elif s == ' ' and current != '':
                words.append(current)
                current = ""
        if current:
            words.append(current)
        
        return ' '.join(words[::-1])
