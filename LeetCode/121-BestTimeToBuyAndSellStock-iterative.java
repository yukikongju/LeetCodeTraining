#!/usr/bin/java

public class Solution{
  public static int maxProfit(int[] prices){
	// One Pass 
	int indexMinPrice = 0;
	int maxProfit = 0;
	for(int i = 1; i<prices.length; i++){
	  int currentProfit = prices[i] - prices[indexMinPrice];
	  if(currentProfit > maxProfit) // update maxProfit if current profit is bigger
		maxProfit = currentProfit;
	  else if(currentProfit < 0) // update indexMinPrice
		indexMinPrice = i;
	}
	return maxProfit;
  }
}
