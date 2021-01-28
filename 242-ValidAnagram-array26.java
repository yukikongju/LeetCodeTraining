#!/usr/bin/java

class Solution {
    public boolean isAnagram(String s, String t) {
        // Increment Array26 with s, decrement with t
        if(s.length() != t.length()) return false;
        int[] counter = new int[26];
        int n = s.length();
        for(int i = 0; i<n ; i++){
            counter[s.charAt(i) -'a']++;
            counter[t.charAt(i) - 'a']--;
        }
        
        for(int count: counter){
            if(count != 0) return false;
        }
        return true;
    }
}
