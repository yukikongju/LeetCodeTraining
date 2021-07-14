// incomplete
class Solution{
    public int[] sortArray(int[] nums){
	// heapsort
	for(int i=0; i<nums.length/2; i++) sink(i);
	int n = nums.length;
	while(n>0){

	}
    }

    public void sink(int[] nums, int i){
	int child = findSmallestChild(i);
	while(child> nums.length && more(i, child)){
	    swap(i, child);
	}
    }

    public int findSmallestChild(int[] nums, int i){
	int left = 2*i+1;
	int right = 2*i+2;
	int smallest = left;
	if(left >= nums.length) return -1;
	if(right < nums.length && less(nums, right, left)) smallest = right;
	return smallest;
    }

    public boolean more(int[] nums, int i, int j){
	return nums[i] > nums[j];
    }

    public boolean less(int[] nums, int i, int j){
	return nums[i] < nums[j];
    }

    public void swap(int[] nums, int i, int j){
	int temp = nums[i];
	nums[i] = nums[j];
	nums[j] = temp;
    }
}
