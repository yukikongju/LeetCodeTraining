#!/usr/bin/java

class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Brute force solution
        for(int i=0; i<nums.length-1; i++){
            for (int j=i+1; j<nums.length; j++){
                if(nums[j] == target - nums[i])
                    return new int[] {i,j};
            }
        } return new int[] {0,0};
    }
}
