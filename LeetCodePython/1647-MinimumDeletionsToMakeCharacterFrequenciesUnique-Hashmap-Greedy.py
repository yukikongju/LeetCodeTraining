#  https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/

class Solution:
    def minDeletions(self, string: str) -> int:
        # solution: Hashmap + greedy


        # --- count dict
        count_dict = defaultdict(int)
        for s in string:
            count_dict[s] += 1
        
        # --- create maxHeap 
        maxHeap = []
        for letter, count in count_dict.items():
            heapq.heappush(maxHeap, (-count, letter))


        # --- greedy: 
        num_removals = 0
        seen = set()
        while maxHeap:
            count, letter = heapq.heappop(maxHeap)
            count *= -1

            while count in seen and count > 0:
                count -= 1
                num_removals += 1
            seen.add(count)

        
        return num_removals


        
