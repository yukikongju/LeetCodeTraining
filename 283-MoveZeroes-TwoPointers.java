class Solution {
    public void moveZeroes(int[] nums) {
	// Two Pointers
	int current=0, next=0;
	if(nums.length != 1){
	    while(next<nums.length){
		if(nums[current] != 0){ // 1er cas: current est valide -> passer au prochain
		    current++;
		    next=current;
		} else if(nums[current] == 0 && nums[next] != 0){ // 2e cas: intervertir les elements
		    nums[current]=nums[next];
		    nums[next]=0;
		    current++;
		    next=current;
		} else {
		    next++;

		}

	    }

	}
    }

}
