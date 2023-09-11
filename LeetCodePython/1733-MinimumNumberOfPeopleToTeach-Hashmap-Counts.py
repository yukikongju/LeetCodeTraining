#  https://leetcode.com/problems/minimum-number-of-people-to-teach/description/

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # solution: Hashmap Counts
        # explanation: https://leetcode.com/problems/minimum-number-of-people-to-teach/solutions/1031079/python-3-steps/

        # --- find people who can't communicate with each other
        individuals = set()
        for x, y in friendships:
            x, y = x-1, y-1
            intersection = set(languages[x]) & set(languages[y])
            if intersection: continue
            else:
                individuals.add(x)
                individuals.add(y)
            
        # --- find most popular language amongst them
        counts = defaultdict(int)
        for individual in individuals:
            for lang in languages[individual]:
                counts[lang] += 1

        # how many person speak the most popular language
        max_count = float('-inf')
        for _, count in counts.items():
            max_count = max(count, max_count)

        # --- teach most popular language to people who don't speak it
        return 0 if max_count == float('-inf') else (len(individuals) - max_count) 
        
