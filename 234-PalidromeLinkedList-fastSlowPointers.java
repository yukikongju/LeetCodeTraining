#!/usr/bin/java

class Solution{
  public boolean isPalindrome(ListNode head){
	// Two Pointers
	// 1. Fast pointer at the end; slow pointer at the middle
	ListNode slow = head, fast = head;
	while(fast != null && fast.next != null){
	  fast = fast.next;
	  slow = slow.next;
	}
	// 2. reverse
	slow = reverse(slow);
	fast = head;
	// 3. compare
	while(slow != null){
	  if(slow.val != fast.val){
		return false;
	  }
	  slow = slow.next;
	  fast = fast.next;
	}
	return true;
  }

  private ListNode reverse(ListNode node){
	// Iterative
	ListNode prev = null;
	ListNode current = node;
	while(current != null){
	  ListNode next = current.next;
	  current.next = prev;
	  prev = current;
	  current = next;
	}
	return prev;
  }
}
