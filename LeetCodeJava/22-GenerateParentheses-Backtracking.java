class Solution {
    public List<String> generateParenthesis(int n) {
	// Backtracking rules: max 3 open and 3 close; close<open
	List<String> output_arr = new ArrayList();
	backtrack(output_arr, "", 0,0, n);
	return output_arr;
    }

    public void backtrack(List<String> output_arr, String current_string, int open, int closed, int max){
	if(current_string.length() == max*2){ // base case
	    output_arr.add(current_string);
	    return;
	}

	if(open<max) backtrack(output_arr, current_string + "(", open+1, closed, max);
	if(closed<open) backtrack(output_arr, current_string  + ")", open, closed+1, max);

    }
}
