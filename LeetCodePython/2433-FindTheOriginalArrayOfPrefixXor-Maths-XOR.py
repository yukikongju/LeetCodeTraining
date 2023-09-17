#  https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # solution: XOR
        # properties of XOR: a ^ b = c <=> a ^ c = b

        # --- base case
        if len(pref) == 1:
            return pref

        # ---
        res = [pref[0]]
        for i in range(len(pref)-1):
            res.append(pref[i] ^ pref[i+1])
        return res 
