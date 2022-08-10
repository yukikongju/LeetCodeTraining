// untested
class Solution{
    public int[] sortArray(int[] nums){
	// mergesort
	return mergesort(nums, 0, nums.length);
    }

    public int[] mergesort(int[] nums, int start, int end){
	if(nums.length == 1) return nums;
	int mid = nums.length/2;
	int[] left = new int[mid];
	int[] right = new int[mid];
	left = mergesort(nums, 0, mid);
	right = mergesort(nums, mid +1, nums.length);
	return fusion(left, right);
    }

    public int[] fusion(int[] left, int[] right){
	int[] sorted = new int[left.length + right.length];
	int i = 0, j = 0, current = 0;
	while(i< left.length && j< right.length){
	    if(left[i] < right[j]) {
		sorted[current++] = left[i++];
	    } else { // right[j] < left[i]
		sorted[current++] = right[j++];
	    }
	}

	// remplir le array si une left ou right n'ont pas la meme longueur
	while(i < left.length) sorted[current++] = left[i++];
	while(j < right.length) sorted[current++] = right[i++];

	return sorted;
    }
}
