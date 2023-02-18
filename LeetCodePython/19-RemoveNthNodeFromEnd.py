#  https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # sol: fast and slow pointer. we start fast pointer n node ahead and iterate through the end
        # cases: 
        # (1) base case: only one node: if head.next == None -> return None
        # (2) remove first node: fast == None -> return head.next 
        # (3) remove node in the middle or at the end -> slow.next = slow.next.next

        # if only one node
        if head.next == None:
            return None

        # start fast pointer ahead
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        
        # check if node we need to remove is the first
        if fast == None: 
            return head.next
            
        # move pointer until the end
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        # remove the node
        slow.next = slow.next.next

        return head


        
