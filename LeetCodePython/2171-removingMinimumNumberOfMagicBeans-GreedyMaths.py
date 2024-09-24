#  https://leetcode.com/problems/removing-minimum-number-of-magic-beans/description/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # solution: Greedy + Math -> histogram
        # trick: we need the remaining bag to form an histogram
        #   because they need to be the same height 
        #   => we need to maximize the size of the rectangle we can form

        beans.sort()
        
        largest = 0
        n = len(beans)
        for i, bean in enumerate(beans):
            largest = max(largest, bean * (n - i))
        return sum(beans) - largest
