#  https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # solution: check if len hashset is the same length of the number of permutations

        # get number of unique binary code of length k
        hashset = set()
        for i in range(len(s)-k+1):
            pattern = s[i:i+k]
            if pattern not in hashset:
                hashset.add(pattern)
        
        print(hashset)
        
        return len(hashset) == 2**k
