class Solution {
    public ListNode oddEvenList(ListNode head) {
	// Iterative
	if(head == null || head.next == null || head.next.next == null) return head;
	ListNode odd = head, even = head.next, headEven = even;

	while(even != null && even.next != null){
	    odd.next = even.next;
	    odd = odd.next;
	    even.next = odd.next;
	    even = even.next;
	}

	odd.next = headEven;
	return head;
    }
}
