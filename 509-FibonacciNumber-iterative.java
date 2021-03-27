class Solution {
    public int fib(int n) {
        // iterative
        if(n == 0 || n == 1) return n;
        int[] tab = new int[n];
        tab[0] = 1;
        tab[1] = 1;
        for(int i = 2; i < n; i++){
            tab[i] = tab[i-1] + tab[i-2];
        }
        return tab[n-1];
    }
}
