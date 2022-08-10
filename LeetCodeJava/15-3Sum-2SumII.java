class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
	// Two Sum II
	Arrays.sort(nums);
	List<List<Integer>> results=new LinkedList<>();

	for(int i=0;i<nums.length-2;i++){
	    if( (i==0) || (i>0 && nums[i] != nums[i-1]) ){
		int target = -1 * nums[i]; // target est l'inverse de l'element
		// call two sum II
		int left=i+1, right = nums.length -1;
		while(left< right){
		    if(nums[left] + nums[right] == target) {
			results.add(Arrays.asList(nums[i], nums[left], nums[right]));
			while(left< right && nums[left] == nums[left+1]) left++;
			while(left <right && nums[right] == nums[right-1]) right--;
			left++;
			right--;
		    }
		    else if(nums[left] + nums[right] < target) left++;
		    else right--;
		}
	    }
	}
	return results;
    }
}
