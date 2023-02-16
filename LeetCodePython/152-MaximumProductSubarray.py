class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP 1D: keep track of max and min values + edge case with 0
        dp_max = [0]*len(nums)
        dp_min = [0]*len(nums)
        dp_max[0] = dp_min[0] = nums[0]
        result = max(nums)
        # current_max = current_min = 1

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp_max[i] = 1
                dp_min[i] = 1
            else: 
                dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
                dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
                result = max(dp_max[i], result)

        # print(dp_max)
        # print(dp_min)

        return result
        
        
