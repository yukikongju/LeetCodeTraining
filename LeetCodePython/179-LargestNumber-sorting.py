from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # --- solution: sorting O(nlogn)

        # convert to str
        nums_str = [str(num) for num in nums]

        def compare(x, y):
            if x + y < y + x:
                return 1
            elif y + x < x + y: 
                return -1
            else: 
                return 0
        
        nums_str.sort(key=cmp_to_key(compare))

        # edge case: first elem is "0" => all nums are 0 => return 0
        return "0" if nums_str[0] == "0" else ''.join(nums_str)
            

        
