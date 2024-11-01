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

