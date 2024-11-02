#  https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # sol: hashmap

        nums.sort()

        # -- insert each number in hashmap where h[sum_digits] = num
        digits_map = defaultdict(list)
        for num in nums:
            digits_sum = sum(int(d) for d in str(num))
            digits_map[digits_sum].append(num)

        # -- compute biggest number
        biggest = -1
        for dsum, dlist in digits_map.items():
            if len(dlist) >= 2:
                biggest = max(biggest, dlist[-1] + dlist[-2])
        
        return biggest
