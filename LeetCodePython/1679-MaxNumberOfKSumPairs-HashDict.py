#  https://leetcode.com/problems/max-number-of-k-sum-pairs/description/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # solution:
        # pop from the back => store index for each number in a hashmap, 
        # and check if difference is still available to be used. If used, set 
        # "used" bool to True and remove from available idx_dct


        idx_dct = defaultdict(list)
        used = [False for _ in range(len(nums))]

        # store index in hashmap
        for i, num in enumerate(nums):
            idx_dct[num].append(i)
        
        # 
        count = 0
        for i, num in enumerate(nums):
            diff = abs(k - num)
            if not used[i] and num + diff == k and len(idx_dct[diff]) > 0 and idx_dct[diff][0] != i:
                used[i] = True
                idx_dct[num].pop(0)
                idx_diff = idx_dct[diff][-1]
                idx_dct[diff].pop(-1)
                used[idx_diff] = True
                count += 1


        return count

