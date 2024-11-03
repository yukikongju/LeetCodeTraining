# Sorting Patterns

**Sorting indices by array values**

nums=[6,0,8,2,1,5]

```{python}
indices = [i for i in range(len(nums))]
indices.sort(key=lambda i: (nums[i], i))

# indices = [1,4,3,5,0,2]
```

