#!/usr/bin/java

class Solution {
    public int singleNumber(int[] nums) {
        // Maths: 2(a+b+c) - (a+a+b+b+c) = c
        HashSet<Integer> hashset = new HashSet<>();
        int sumOfDiffNums = 0, sumOfAllNums = 0;
        
        for(int i=0; i<nums.length; i++){
            // ajouter num differents
            if(!hashset.contains(nums[i])){
                hashset.add(nums[i]);
                sumOfDiffNums += nums[i];
            }
            // ajouter all num
            sumOfAllNums += nums[i];
        }
        return 2* sumOfDiffNums - sumOfAllNums;
    }    
}
