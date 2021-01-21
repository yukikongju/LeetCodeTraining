#!/usr/bin/java

class Solution {
    public void reverseString(char[] s) {
        // Recursive Solution
        reverse(s, 0, s.length -1);
    }
    
    private void reverse(char[] s, int left, int right){
        if(left >= right) return ;
        char temp = s[left];
        s[left++] = s[right];
        s[right--] = temp;
        reverse(s, left, right);
    }
}
