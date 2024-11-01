#  https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # solution: prefix sum + hashmap
        # we calculate prev sum and post sum

        
        #
        values_dct = defaultdict(list)
        for i, num in enumerate(nums):
            values_dct[num].append(i)
        
        #
        sol = [0 for _ in range(len(nums))]
        for value, indexes in values_dct.items():
            total_sum = sum(indexes)
            pre_sum = 0
            n = len(indexes)
            for pos, index in enumerate(indexes):
                post_sum = total_sum - pre_sum - index
                prev_sum = index * pos - pre_sum
                post_sum = post_sum - index * (n - pos - 1)
                pre_sum += index
                sol[index] = prev_sum + post_sum

        return sol
