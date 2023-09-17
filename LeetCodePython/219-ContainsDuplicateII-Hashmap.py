#  https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # solution: hashmap

        # ---
        num_dict = defaultdict(list)
        for i, num in enumerate(nums):
            num_dict[num].append(i)
            if len(num_dict[num]) >= 2 and (num_dict[num][-1] - num_dict[num][-2] <= k):
                return True
        return False
        

