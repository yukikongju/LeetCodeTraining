#  https://leetcode.com/problems/continuous-subarray-sum/description/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # solution: prefix sum
        # modulo properties: 
        # - addition: (a+b) mod n = a mod n + b mod n
        # what is the remainder needed to complete

        # base case
        if len(nums) == 1:
            return False

        prefix_sum = 0
        freq_dct = {0: -1} # remember index of last remainder
        for j, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in freq_dct:
                if j - freq_dct[remainder] >= 2:
                    return True
            else:
                freq_dct[remainder] = j

        return False
