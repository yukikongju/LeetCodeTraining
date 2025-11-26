#  https://leetcode.com/problems/time-based-key-value-store/description/
# Solution: Binary Search O(log n)
# Strategy:
# - save the best candidate so far

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        left, right = 0, len(arr) - 1
        res = ""

        while (left <= right):
            mid = (left + right) // 2
            t, v = arr[mid]

            if t == timestamp:
                return v
            
            if t <= timestamp:
                res = v
                left = mid + 1
            else:
                right = mid - 1
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
