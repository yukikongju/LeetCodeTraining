#  https://leetcode.com/problems/count-the-number-of-good-subarrays/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # solution: frquency count + sliding window
        # intuition: 
        # 

        freq = defaultdict(int)
        pair_count, ans, left = 0, 0, 0

        for right in range(len(nums)):
            pair_count += freq[nums[right]]
            freq[nums[right]] += 1

            while pair_count >= k:
                ans += len(nums) - right
                freq[nums[left]] -= 1
                pair_count -= freq[nums[left]]
                left += 1
        
        return ans
