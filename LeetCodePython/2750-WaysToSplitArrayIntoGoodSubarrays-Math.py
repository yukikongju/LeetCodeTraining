#  https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/description/

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # solution: 
        # idea: count the number of 0s before the 1s and multiply them

        # edge case: remove zeros starting and ending nums because they 
        #   cannot be used for additional subarrays
        s = "".join([str(n) for n in nums])
        s = s.strip("0")

        # edge case:
        if len(s) == 0:
            return 0

        # count number of 0s between 1s 
        count = 0
        zeros = [] 
        for num in s:
            if num == "0":
                count += 1
            else:
                if count > 0:
                    zeros.append(count + 1)
                count = 0

        # compute subarrays
        product = 1
        for num in zeros:
            product *= num % (10 ** 9 + 7)

        return product % (10 ** 9 + 7)
