def prefix_sum(nums):
    n = len(nums)
    prefixes = [0] * (n+1)

    for i in range(n):
        prefixes[i+1] = prefixes[i] + nums[i]
