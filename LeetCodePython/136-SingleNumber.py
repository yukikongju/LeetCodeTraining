#  https://leetcode.com/problems/single-number/description/
#  NeetCode:

# Solution 1: use hashmap to count the numberw of occurences
# Space: O(n); Time: O(n) (first loop to count occurences; second loop to 
# find unique element)

# Solution 2: Use XOR 
# Space: O(1); Time: O(n)


def singleNumber1(nums):
    # remplir le dictionnaire
    counts = {}
    for n in nums:
        if n not in counts:
            counts[n] = 1
        else: 
            counts[n] += 1
    
    # find unique element
    for n in nums: 
        if counts[n] == 1:
            return n


def singleNumber2(nums):
    res = 0
    for num in nums: 
        res = res ^ num
    return res

