class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
	// Walker-Runner Method

	// runner should be n+1 nodes ahead
	ListNode dummy = new ListNode(0);
	dummy.next = head;
	ListNode walker = dummy;
	ListNode runner = dummy;
	int i=0;
	while(i<n+1){ // décaler le runner de n+1 nodes
	    runner = runner.next;
	    i++;
	}

	while(runner !=null){ //find the node before the one we should remove
	    runner = runner.next;
	    walker = walker.next;
	}

	// remove the node
	walker.next = walker.next.next;

	return dummy.next;
    }

}
