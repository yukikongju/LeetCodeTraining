# Prefix Sum Pattern

**Computing sum of absolute values**

Ex: [1,3,5] => |3-1| + |3-3| + |5-3| = ans

```
prefix_sum = [0,1,4,9]
val=3; idx=2 ; n=len(nums)=3
post_sum = (total_sum - prefix_sum[idx]) - val * (n-idx)
prev_sum = val * idx - prefix_sum[idx]
ans = post_sum + prev_sum
```

**Continuous Subarray Sum**

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.


Idea: remember index of remainder


```{python}
prefix_sum = 0
freq_dct = {0: -1} # remember index of last remainder
for j, num in enumerate(nums):
    prefix_sum += num
    remainder = prefix_sum % k
    if remainder in freq_dct:
	if j - freq_dct[remainder] >= 2:
	    return True
    else:
	freq_dct[remainder] = j
```

