class Solution{
    public int[] sortArray(int[] nums){
	// insertion sort
	for(int i=0; i<nums.length; i++){
	    for(int j=i; j>0 && (nums[j] < nums[j-1]); j--){
		swap(nums, j, j-1);
	    }
	}
	return nums;
    }

    public void swap(int[] nums, int i, int j){
	int temp = nums[i];
	nums[i] = nums[j];
	nums[j] = temp;
    }
}
