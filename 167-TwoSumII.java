class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Brute-Force
        for(int i=0; i < numbers.length; i++){
            for(int j=i+1; j < numbers.length; j++){
                if ( (numbers[i] + numbers[j]) == target){
                    int output[] = {i+1,j+1};
                    return output;
                }
            }
        }
        return null;
    }
}
