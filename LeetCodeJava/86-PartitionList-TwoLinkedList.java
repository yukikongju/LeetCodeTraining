class Solution {
    public ListNode partition(ListNode head, int x) {
	// Two Pointers: loop trough linked list and create node smaller; node bigger; link them together at the end
	ListNode smaller = new ListNode(0);
	ListNode greater = new ListNode(0);
	ListNode dummy = smaller;
	ListNode greaterHead = greater;
	ListNode current = head;
	while(current != null){
	    ListNode next = current.next;
	    if(current.val<x){
		smaller.next = current;
		smaller = smaller.next;
	    } else { //current.val>= x
		greater.next = current;
		greater = greater.next;
	    }
	    current = next;
	}

	greater.next = null;

	// link greater list after smaller
	smaller.next = greaterHead.next;

	return dummy.next;
    }
}
