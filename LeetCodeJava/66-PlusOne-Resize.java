class Solution {
    public int[] plusOne(int[] nums) {
	// 1er cas: retenue sans resize le array
	int pos=nums.length-1;
	for(int i=nums.length-1; i>=0; i--){
	    if(nums[i] !=9){
		nums[i]++;
		return nums;
	    } else {
		nums[i]=0;
	    }
	}

	// 2e cas: dernier spot a une retenue -> resize array
	int[] newNums=new int[nums.length+1];
	newNums[0]=1;
	newNums[1]=0;
	for(int i=1; i<nums.length; i++){
	    newNums[i+1] = nums[i];
	}

	return newNums;
    }
}
