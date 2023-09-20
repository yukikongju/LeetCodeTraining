#  https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def compress(self, chars: List[str]) -> int:
        # solution: pointer

        # ---
        n = len(chars)
        res = []
        count = 1
        for i in range(1, n):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                res.append(chars[i-1])
                if count > 1: res.append(str(count))
                count = 1
        res.append(chars[n-1])
        if count > 1: res.append(str(count))

        # --- replace input array
        string = ''.join(res)
        for i, s in enumerate(string):
            chars[i] = s


        return len(string) 


