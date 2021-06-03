#!/usr/bin/java

class Solution {
    public int removeDuplicates(int[] nums) {
	// Two Pointers
	int count=0, prev=0, next=0;
	if(nums.length==0) return 0;
	while(next<nums.length){
	    if(nums[prev]!=nums[next]){
		nums[prev+1]=nums[next];
		prev++;
		count++;

	    }
	    next++;

	}
	return count+1;
    }
}
