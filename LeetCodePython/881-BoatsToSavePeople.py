#  https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # solution: sort values and iterate until pointer cross (pointers)
        people.sort()

        count = 0 
        left, right = 0, len(people) -1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            count += 1

        return count
