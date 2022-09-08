#  Link: https://leetcode.com/problems/two-sum/

# Reformulation: You are playing D&D with your friend and in order to survive, 
# you need to slay the dragon, which requires you to deal exactly 16 damage. 
# On your turn, you only roll an 8. Fortunately, one of your comarades plays 
# a spell card, which allows all the team member to roll a dice and combine 
# their attack with yours. Your team member roll respectively 1,5,7,8,12. 
# Are you able to slay the dragon? If so, with which team member did you 
# make the combined attacked?


# Time Complexity: O(n) => we iterate through nums one time and hashmap lookup 
# takes O(1) 

# Solution: check if difference is in hashmap

# Follow Up: Now, the dragon has entered rage mode and requires exactly 32 damage 
# to be defeated. Another teamate of your plays a card that allows your team 
# to create a three way attack to the dragon. Your teamates roll respectively 
# 12, 6, 15, 3. Are you still able to defeat the dragon? If so, who was the 
# third member of the attack? (3Sum)

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
        
