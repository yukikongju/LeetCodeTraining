#!/usr/bin/java

class Solution {
    public int maxArea(int[] height) {
	  // sliding window technique
	  if (height.length <= 1)
		  return -1;
	  int left = 0, right = height.length -1;
	  int maxVol = 0; // vol = base x hauteur
	  while (left < right){
		  // calcul du volume
		  int base = right - left;
		  int hauteur = Math.min(height[left], height[right]);
		  int tempVol = base * hauteur;
		  maxVol = Math.max(tempVol, maxVol);
		  // decider l'index a incrementer/decrementer
		  if(height[left] < height[right]){
			  left++;
		  }else{
			  right--;
		  }
	  }
	  return maxVol;
    }
}
