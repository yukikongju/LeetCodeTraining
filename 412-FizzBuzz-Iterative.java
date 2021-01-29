#!/usr/bin/java

class Solution {
    public List<String> fizzBuzz(int n) {
        // Iterative
        List<String> shout = new ArrayList<>();
        for(int i=1; i<= n; i++){
            if(i % 3 == 0 && i % 5 == 0)
                shout.add("FizzBuzz");
            else if(i%3==0)
                shout.add("Fizz");
            else if(i%5==0)
                shout.add("Buzz");
            else
                shout.add(Integer.toString(i));
        }
        return shout;
    }
}
