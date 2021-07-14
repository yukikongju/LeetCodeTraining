class Solution {
    public int coinChange(int[] coins, int amount) {
	/* Dynamic Programming: unbounded knapsack */
	int[] dp = new int[amount+1];
	dp[0] = 0;

	// calculate dp
	for(int i=1; i<=amount; i++){ // iterate through all amounts
	    dp[i] = Integer.MAX_VALUE;
	    for(int coin: coins){ // update for all coins
		if(i-coin>=0 && dp[i-coin] != Integer.MAX_VALUE)
		    dp[i] = Math.min(dp[i-coin]+1, dp[i]);
	    }
	}

	// check if amount of coins exists
	if(dp[amount] == Integer.MAX_VALUE){
	    return -1;
	} else {
	    return dp[amount];
	}

    }
}
