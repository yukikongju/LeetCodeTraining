public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
	// Catching Up: the first loop is done so that they are in sync

	if(headA == null || headB == null) return null;

	ListNode pointer_a = headA;
	ListNode pointer_b = headB;

	while(pointer_a != pointer_b){
	    if(pointer_a == null) {
		pointer_a = headB; // no intersection
	    } else{
		pointer_a = pointer_a.next;
	    }

	    if(pointer_b == null){
		pointer_b = headA;
	    } else{
		pointer_b = pointer_b.next;
	    }
	}

	return pointer_a; // or pointer_b : return null or the intersection

    }
}
