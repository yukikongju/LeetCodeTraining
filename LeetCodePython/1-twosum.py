class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sol: check if difference is in hashmap
        
        hashmap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashmap.keys():
                return [i, hashmap.get(difference)]
            else:
                hashmap[num] = i
        
