#  https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # solution: math + pointer
        # (1) sort
        # (2) compute skill level: skill level = sum(skill) / (n/2) ; n = len(skill) => if skill level not int, then -1
        # (3) use pointer to get chemistry level

        # 1. sort 
        skill.sort() 

        # 2. compute skill level
        n = len(skill)
        if sum(skill) % (n / 2) != 0:
            return -1
        skill_level = sum(skill) // (n / 2)

        # 3. compute chemistry
        chemistry = 0
        left, right = 0, len(skill) - 1
        while left < right: 
            if (skill[left] + skill[right] != skill_level):
                return -1 
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry

