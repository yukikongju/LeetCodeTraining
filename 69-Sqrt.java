class Solution {
    public int mySqrt(int x) {
        double square = Math.sqrt(x);
        int trunc = (int) square;
        return trunc;
    }
}
