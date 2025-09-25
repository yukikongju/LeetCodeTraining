from typing import List

def binary_search(arr: List[int], val: int) -> bool:
    left, right = 0, max(arr)
    while left < right:
        mid = left + (right - left) // 2
        if mid == val:
            return True
        if val < mid:
            right = mid
        else:
            left = mid + 1
    return False

