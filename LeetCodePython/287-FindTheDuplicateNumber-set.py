#  Link: https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Sol: set => add num if not in set, else return num O(n)
        duplicates = set()
        for num in nums: 
            if num not in duplicates:
                duplicates.add(num)
            else: 
                return num
        
