class Solution {
    public int fib(int n) {
	// sequential solution
        if(n == 0 || n == 1) return n;
        if(n == 2) return 1;
        int current = 0;
        int prev1 = 1;
        int prev2 = 1;

        int i = 3;

        do{
            i++;
            current = prev1 + prev2;
            prev2 = prev1;
            prev1 = current;
        } while(i<=n);

        return current;
    }
}
