#  https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solution: Fast and slow pointer

        # -- base case
        if not head or not head.next:
            return None

        # --- fast and slow pointer to find middle node
        dummy = head
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # --- delete middle node
        slow.next = slow.next.next

        return dummy
