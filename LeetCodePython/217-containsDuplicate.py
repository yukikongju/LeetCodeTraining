class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sol: add item to set if not in 
        
        hashset = set()
        for num in nums: 
            if num in hashset:
                return True
            hashset.add
        return False
    
    
