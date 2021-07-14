#!/usr/bin/java

public class Solution{
  public static int maxProfit(int[] prices){
      // Keep minValue in auxiliary and update maxProfit
      int minValue = prices[0], maxProfit = 0;
      for(int i=1; i<prices.length; i++){
          if(minValue < prices[i])
              maxProfit = Math.max(maxProfit, prices[i] - minValue);
          else
              minValue = prices[i];
      }
      return maxProfit;
  }
}
