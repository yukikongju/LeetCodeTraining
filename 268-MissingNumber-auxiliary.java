#!/usr/bin/java

class Solution {
    public int missingNumber(int[] nums) {
        // Use Array as auxiliary to count
        int[] count = new int[nums.length+1];
        // count occurence
        for(int i=0; i<nums.length; i++){
            count[nums[i]] = 1;
        }
        // check if number missing
        for(int i=0;i<count.length; i++){
            if(count[i] != 1) return i;
        }
        return nums.length+1;
    }
}
