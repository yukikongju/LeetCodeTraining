#!/usr/bin/java

class Solution {
    public void rotate(int[] nums, int k) {
        // Brute Force
        for(int i=0; i<k; i++){
            int prev = nums[nums.length-1];
            for(int j=0; j < nums.length; j++){
                int temp = nums[j];
                nums[j] = prev;
                prev = temp;
            }
        }
    }
}
