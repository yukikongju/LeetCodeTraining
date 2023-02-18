#  https://leetcode.com/problems/add-two-numbers/description/# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # solution: 

        head = ListNode()
        current = head
        
        # append node
        remainder = 0
        while l1 or l2:
            current_sum = remainder 
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val 
                l2 = l2.next
            
            node_val = current_sum % 10
            remainder = current_sum // 10

            node = ListNode(node_val)
            current.next = node
            current = current.next


        # if remainder, add additional node 
        if remainder != 0:
            node = ListNode(1)
            current.next = node

        return head.next
