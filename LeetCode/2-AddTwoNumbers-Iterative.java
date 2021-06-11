class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
	// Iterative
	ListNode head = new ListNode(0);
	ListNode node1 = l1, node2 = l2, current = head;
	int carry = 0;
	while(node1 != null || node2 != null){
	    int x = (node1 != null) ? node1.val : 0;
	    int y = (node2 != null) ? node2.val : 0;
	    int sum = carry + x + y;
	    carry = sum /10;
	    ListNode newNode = new ListNode(sum%10);
	    current.next = newNode;
	    current = current.next;
	    if(node1 != null) node1 = node1.next;
	    if(node2 != null) node2 = node2.next;
	}

	if(carry == 1){
	    current.next = new ListNode(1);
	}

	return head.next;
    }
}
