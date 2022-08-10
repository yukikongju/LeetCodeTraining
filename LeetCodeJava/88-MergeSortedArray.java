class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int pos1 = m - 1, pos2 = n - 1, pos_merged = m + n -1;
        int []merged_array = new int[m + n];
        while(pos1 >= 0 && pos2 >= 0){
            nums1[pos_merged--] = nums1[pos1] > nums2[pos2] ? nums1[pos1--] : nums2[pos2--];
        }
        while(pos2 >= 0){
            nums1[pos_merged--] = nums2[pos2--];
        }
    }
}
