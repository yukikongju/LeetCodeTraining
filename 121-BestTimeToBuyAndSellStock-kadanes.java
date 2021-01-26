#!/usr/bin/java

// runtime: 3ms -> bad

public class Solution{
  public static int maxProfit(int[] prices){
	// Kadane's Algoritm
	int maxProfit = 0;
	int cheapestStock = prices[0];
	for(int i=1; i<prices.length; i++){
	  int currentProfit = prices[i] - prices[i-1];
	  maxProfit = Math.max(currentProfit, maxProfit);
	  prices[i] = Math.min(prices[i], prices[i-1]);
	}
	return maxProfit;
  }
}
