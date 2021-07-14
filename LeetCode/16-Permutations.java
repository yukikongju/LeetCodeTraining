class Solution {
    public List<List<Integer>> permute(int[] nums) {
	// Backtracking
	List<List<Integer>> output=new ArrayList<>();
	backtrack(output, nums, 0);
	return output;
    }

    public void backtrack(List<List<Integer>> output, int[] nums, int start){
	if(start == nums.length){ // base case: add number to array
	    output.add(toList(nums));
	    return;
	} else {
	    for(int i = start; i < nums.length; i++){
		swap(i, start, nums);
		backtrack(output, nums, start+1);
		swap(i, start, nums);
	    }
	}

    }

    public List<Integer> toList(int[] nums){
	List<Integer> result = new ArrayList<>();
	for(int i: nums){
	    result.add(i);

	}
	return result;

    }

    public void swap(int i, int j, int[] nums){
	int temp = nums[i];
	nums[i] = nums[j];
	nums[j] = temp;

    }


}
