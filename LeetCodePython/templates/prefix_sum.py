def prefix_sum(nums, l, r):
    n = len(nums)
    prefixes = [0] * (n+1)

    for i in range(n):
        prefixes[i+1] = prefixes[i] + nums[i]

    # sum of nums[l..r]
    ranged_sum = prefixes[r+1] - prefixes[l]

    return ranged_sum
