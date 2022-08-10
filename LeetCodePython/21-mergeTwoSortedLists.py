# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Sol: Keep two pointers and add remaining
        
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        head = ListNode()
        dummy = head
        # p1, p2 = list1, list2
        
        # compare with pointers until one is finished
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else: 
                head.next = list2
                list2 = list2.next
            head = head.next
        
        # add remaining
        if list1: 
            head.next = list1
        if list2:
            head.next = list2
        
        return dummy.next
