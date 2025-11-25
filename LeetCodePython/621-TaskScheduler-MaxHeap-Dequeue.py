#  https://leetcode.com/problems/task-scheduler/description/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Solution: MaxHeap + Dequeue
        # Notes:
        # - Use heap to get next available task, prioritizing task with highest unit
        # - Use queue to keep track task cooldown, and put back to heap once cooldown is up

        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)
        cooldown = deque() # (next_available_time, count)
        time = 0

        while len(maxHeap) > 0 or len(cooldown) > 0:
            time += 1

            # check next task to execute in heap
            if len(maxHeap) > 0:
                count = heapq.heappop(maxHeap)
                count += 1 # decreased number of tasks left, but increments since maxHeap
                if count != 0: # need to cooldown
                    cooldown.append((time + n, count))

            # check if task has cooldown
            if cooldown and cooldown[0][0] <= time:
                _, c = cooldown.popleft()
                heapq.heappush(maxHeap, c)

        return time

