class Solution {
    public ListNode swapPairs(ListNode head) {
	// Walker-Runner Method

	ListNode dummy = new ListNode(0);
	dummy.next = head;
	ListNode runner = dummy;

	while(runner.next != null && runner.next.next != null){
	    ListNode r1 = runner.next;
	    ListNode r2 = runner.next.next;

	    // swap pointers
	    runner.next = r2;
	    r1.next = r2.next;
	    r2.next = r1;

	    // move runner
	    runner = runner.next.next;
	}

	return dummy.next;
    }
}
