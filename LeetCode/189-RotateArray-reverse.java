#!/usr/bin/java

class Solution {
    public void rotate(int[] nums, int k) {
        // Reverse Solution
		// 1. Reverse whole array
		// 2. Reverse from first to k element
		// 3. Reverse from k to last element
        k = k % nums.length;
        reverse(nums, 0, nums.length -1);
        reverse(nums, 0, k-1);
        reverse(nums, k, nums.length -1);
    }
    
    private void reverse(int[] nums, int start, int end){
        while (start < end){
            int temp = nums[start];
            nums[start++] = nums[end];
            nums[end--] = temp;
        }
    }
}
