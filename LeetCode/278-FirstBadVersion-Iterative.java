/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        // Iterative starting from last O(n) (too slow)
        for(int i=n; i>=0 ; i--){
            if(!isBadVersion(i)) return i+1;
        }
        return 0;
    }
}
