#  https://leetcode.com/problems/target-sum/submissions/1570389588/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # solution: cache number of times

        n = len(nums)
        counts = defaultdict(int)
        counts[0] = 1
        
        for num in nums:
            updated_counts = defaultdict(int)
            for key, value in counts.items():
                updated_counts[key - num] += value
                updated_counts[key + num] += value
            counts = updated_counts

        return counts[target]
