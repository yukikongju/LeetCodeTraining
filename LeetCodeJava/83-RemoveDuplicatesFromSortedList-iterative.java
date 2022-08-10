#!/usr/bin/java

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        // Compare current with next
        ListNode current = head;
        while(current != null && current.next != null){
            if(current.next.val == current.val){
                // consecutive values -> remove
                ListNode grandchild = current.next.next;
                current.next = grandchild; // make grandchild as next node
            } else {
                current = current.next;
            }
        }
        return head;
    }
}
