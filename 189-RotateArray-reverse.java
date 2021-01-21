#!/usr/bin/java

class Solution {
    public void rotate(int[] nums, int k) {        
        // Using Reverse
        // 1. Reverse array
        // 2. Reverse first k element
        // 3. Reverse n-k element
        reverse(nums, 0, nums.length -1);
        reverse(nums, 0, k -1);
        reverse(nums, k, nums.length -1);
    }
    
    private void reverse(int[] nums, int left, int right){
        while(left < right){
            int temp = nums[left];
            nums[left++] = nums[right];
            nums[right--] = temp;
        }
    }
}
