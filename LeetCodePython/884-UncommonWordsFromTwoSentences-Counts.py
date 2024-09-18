from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # -- solution: 
        # 1. convert string to list of words
        # 2. for each string, count the number of occurences for each word
        # 3. compare counts for each word => take the min => if 0, then it is a uncommon word

        # 1. 
        l1 = s1.split()
        l2 = s2.split()
        
        # 2.
        def count(l: [str]):
            c = defaultdict(int)
            for w in l:
                c[w] += 1
            return c
        c1 = count(l1)
        c2 = count(l2)

        # 3. 
        words = set(l1 + l2)
        uncommon_words = []
        for word in words:
            min_count = min(c1[word], c2[word])
            if (c1[word] == 0 and c2[word] == 1) or (c1[word] == 1 and c2[word] == 0):
                uncommon_words.append(word)

        return uncommon_words

        
