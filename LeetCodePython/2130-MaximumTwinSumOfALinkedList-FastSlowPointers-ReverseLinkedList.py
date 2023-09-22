#  https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # solution: Fast Slow pointer ; reverse
        # iterate start -> mid ; end -> mid 

        # --- fast and slow pointers to find mid 
        first = head
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # --- reverse second half
        second = slow.next
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev

        # --- find max twin
        max_twin = float('-inf')
        while second:
            twin = first.val + second.val 
            max_twin = max(twin, max_twin)
            first, second = first.next, second.next

        # return max_twin 
        return max_twin

        
