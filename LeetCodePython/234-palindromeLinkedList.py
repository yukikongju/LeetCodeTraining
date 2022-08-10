# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Sol: Reverse Linked list from the end and compare head and last
        
        # base case
        if not head.next:
            return True
        
        # get mid
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse from mid (slow pointer)
        fast = head
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        slow = prev
        
        # compare
        while fast and slow: 
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        
        return True
            
