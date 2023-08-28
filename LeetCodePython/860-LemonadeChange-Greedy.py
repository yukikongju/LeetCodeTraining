#  https://leetcode.com/problems/lemonade-change/description/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # solution: greedy
        bills_5, bills_10 = 0, 0

        # --- give out 10$ first, then 5$
        for bill in bills:
            if bill == 5:
                bills_5 += 1
            elif bill == 10:
                bills_5 -= 1
                bills_10 += 1
            else: # bill == 20
                if bills_10 >= 1:
                    bills_10 -= 1
                    bills_5 -= 1
                else: # no 10$ bill
                    bills_5 -= 3
            
            if bills_5 < 0 or bills_10 < 0:
                return False
  
        # ---
        return True


