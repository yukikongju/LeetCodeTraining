class Solution {
    public String longestPalindrome(String s) {
	// Expending from middle: extend palindrome from current position

	String longestSubstring = "";

	for(int i=0;i<s.length();i++){
	    // odd length
	    int left=i, right=i;
	    while(left>=0 && right<s.length()){
		String substring = s.substring(left, right+1);
		if(s.charAt(left) == (s.charAt(right))){
		    if(substring.length()>longestSubstring.length()) longestSubstring=substring;
		    left--; right++;
		} else{
		    break;
		}
	    }

	    // even length
	    left=i; right=i+1;
	    while(left>=0 && right<s.length()){
		String substring = s.substring(left, right+1);
		if(s.charAt(left) == (s.charAt(right))){
		    if(substring.length()>longestSubstring.length()) longestSubstring=substring;
		    left--; right++;
		} else{
		    break;
		}
	    }
	}
	return longestSubstring;
    }
}
