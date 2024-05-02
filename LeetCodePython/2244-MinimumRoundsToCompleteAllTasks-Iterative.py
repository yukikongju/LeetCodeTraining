class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # solution: iterative
        # 1) divisible with only 3s
        # 2) divisible with only 2s
        # 3) divisible with both 3s and 2s
        # note: only freq of 1 is not

        # --- counter
        counter = Counter(tasks)

        # ---
        rounds = 0
        for key in counter:
            count = counter[key]
            if count == 1:
                return -1
            else:
                rounds += ceil(count / 3)

        return rounds
