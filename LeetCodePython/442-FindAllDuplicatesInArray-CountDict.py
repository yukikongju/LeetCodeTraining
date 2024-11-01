#  https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # solution: dict count
        
        # count occurences for each number
        count_dct = defaultdict(int)
        for num in nums:
            count_dct[num] += 1
        
        # add number with 2 occurences in output array
        out = []
        s = set(nums)
        for num in s:
            if count_dct[num] == 2:
                out.append(num)
        return out
