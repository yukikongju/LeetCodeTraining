#  https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # solution: math => O(n) & sort: O(nlogn)
        # find the middle elements and sum abs values
        # res = sum | xi - midVal |

        nums.sort()
        midVal = nums[len(nums) // 2]
        res = sum([abs(x - midVal) for x in nums])
        return res
