#  https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/description/

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        # solution: greedy + modulo
        # always add/substract limit, until smaller

        # --- sum given in array
        total = 0
        for num in nums:
            total += num

        # --- 
        difference = abs(goal - total)
        num_elements = difference // limit
        remainder = difference % limit
        if remainder != 0:
            num_elements += 1
        
        return num_elements

