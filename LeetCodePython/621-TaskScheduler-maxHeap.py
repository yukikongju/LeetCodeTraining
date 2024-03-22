from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # solution: maxHeap [cnt, idle]
        # if in heap: items to be processed
        # if in queue: add back to heap bc they can be processed again

        # --- count the number of tasks
        c = Counter(tasks)
        maxHeap = [-cnt for cnt in c.values()]
        heapq.heapify(maxHeap)

        # ---
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
