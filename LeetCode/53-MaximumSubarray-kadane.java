#!/usr/bin/java

class Solution{
  public void maxSubArray(int[] nums){
	// Kadane's Algorithm
	int maxSum = nums[0];
	int currentSum = maxSum;
	for(int i = 1; i< nums.length; i++){
	  currentSum = Math.max(nums[i], nums[i] + currentSum); // start over or add element
	  maxSum = Math.max(currentSum, maxSum); // update maxSum if current is bigger
	}
	return maxSum;
  }
}
