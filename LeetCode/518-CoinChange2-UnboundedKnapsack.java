class Solution {
    public int change(int amount, int[] coins) {
	// Dynamic Programming: bounded Knapsack

	int[] dp=new int[amount+1]; // store the number of combinations
	dp[0] =1;

	// calculate number of combinations: how many ways to compute dp[i] with previous coin
	for(int coin: coins){
	    for(int i=coin; i<=amount; i++){
		dp[i] += dp[i-coin];
	    }
	}

	return dp[amount];
    }
}
