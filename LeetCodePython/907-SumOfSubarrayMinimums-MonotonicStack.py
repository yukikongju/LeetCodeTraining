#  https://leetcode.com/problems/sum-of-subarray-minimums/?envType=problem-list-v2&envId=monotonic-stack

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # naive: brute force O(n^2)
        # solution: monotonic stack O(n) => https://www.youtube.com/watch?v=aX1F2-DrBkQ
        # intuition: we store the index of the minimum values before i 
        # - how many subarrays exist where arr[i] is the minimum
        # (i - j) => number of subrrays at the right that have arr[i] as the minimum
        # res[j] => sum of subarray minimum for all subarrays ending at j

        n = len(arr)
        MOD = 10**9 + 7
        res = [0] * (n+1)
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            prev_index = stack[-1] if stack else -1 
            res[i] = (res[prev_index] + (i - prev_index) * arr[i]) % MOD
            stack.append(i)
        
        return sum(res) % MOD
