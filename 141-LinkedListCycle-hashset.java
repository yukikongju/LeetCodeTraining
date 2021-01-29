#!/usr/bin/java

class Solution{
  public boolean hasCycle(ListNode head){
    HashSet<ListNode> hashset = new HashSet<>();
    while(head != null){
      if(hashset.contains(head)){
	return true;
      }
      hashset.add(head);
      head = head.next;
    }
    return false;
  }
}
