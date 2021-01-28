#!/usr/bin/java

class Solution {
    public int singleNumber(int[] nums) {
        // Push and pop with Auxiliary
        List<Integer> list = new ArrayList<>();
        for(int i=0; i< nums.length; i++){
            if(list.contains(nums[i])){
                list.remove(new Integer(nums[i]));
            } else { // doesn't contains num
                list.add(nums[i]);
            }
        }
        return list.get(0);
    }    
}
