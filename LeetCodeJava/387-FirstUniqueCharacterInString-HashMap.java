class Solution {
    public int firstUniqChar(String s) {
	/* HashMap Solution */
	HashMap<Character, Integer> hashmap = new HashMap<>();
	int n = s.length();
	// add the number to hashmap
	for(int i=0; i<n; i++){
	    char c = s.charAt(i);
	    hashmap.put(c, hashmap.getOrDefault(c,0) + 1);
	}

	// find the first occurence
	for(int i=0; i<n; i++){
	    if(hashmap.get(s.charAt(i)) == 1) return i;
	}
	return -1;
    }
}
