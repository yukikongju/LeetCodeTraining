#!/usr/bin/java

class Solution {
    public boolean isPalindrome(String s) {
        // Two pointers
        if(s.length() == 0 || s.length() == 1) return true; //trivial
        s = s.replaceAll("[^a-zA-Z0-9]*", "").toLowerCase();
        int left = 0, right = s.length() -1;
        while(left < right){
            if(s.charAt(left++) != (s.charAt(right--))) return false;
        }
        return true;
    }
}
