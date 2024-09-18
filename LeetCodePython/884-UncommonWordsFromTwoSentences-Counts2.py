from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # -- solution: uncommon words will only appear once in both string O(n)

        # 
        l1 = s1.split()
        l2 = s2.split()
        words = l1 + l2

        #
        c = Counter(words)

        # 
        return [word for word in c if c[word] == 1]

        
