#!/usr/bin/java

class Solution{
  public LisNode reverseListNode(ListNode head){
	// Recursive Solution
	if(head == null || head.next == null) return head;
	ListNode p = reverseListNode(head.next);
	head.next.next = head;
	head.next = null;
	return p;
  }
}
