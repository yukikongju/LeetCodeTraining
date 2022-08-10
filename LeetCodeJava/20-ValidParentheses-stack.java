#!/usr/bin/java

class Solution {
    public static char[][] TOKENS = {{'{','}'}, {'[',']'}, {'(',')'}};
    
    public boolean isValid(String s) {
        if(s.length() == 0) return true;
        if(s == null) return false;
        
        Stack<Character> stack = new Stack<>();
        
        for(int i = 0; i < s.length(); i++){
            if(isOpen(s.charAt(i))){
                stack.push(s.charAt(i));
            } else {
                if(stack.isEmpty() || !matches(stack.pop(), s.charAt(i))){
                    return false;
                }
            }
        }
        return stack.isEmpty();
        }
    
    public boolean isOpen(char c){
        for(char[] array: TOKENS){
            if(array[0] == c) return true;
        }
        return false;
    }
    
    public boolean matches(char pop, char c){
        for(char[] array: TOKENS){
            if(array[0] == pop && array[1] == c) return true;
        }
        return false;
    }
}
