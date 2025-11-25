#  https://leetcode.com/problems/task-scheduler/submissions/1839722869/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Solution: Frequency
        # Notes:
        # 1. Count how many times each task appear
        # 2. Count:
        #     - max_freq => highest frequency of any tasks
        #     - num_max => number of tasks with highest frequency ie max_freq
        # 3. Place most frequent tasks first
        # Ex: ["A","A","A","B","B","B"] => {'A': 3, 'B': 3}
        # A _ _ A _ _ A _ _ ; A B _ A B _ A B _ ; we can place the remainder however we want
        # if there is no idle time, then res = len(tasks)

        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1

        max_freq = max(counts.values())
        num_max = sum([1 for _, v in counts.items() if v == max_freq])

        num_parts = max_freq - 1
        part_size = n + 1
        res = num_parts * part_size + num_max

        return max(res, len(tasks))
