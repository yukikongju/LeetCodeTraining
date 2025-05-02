# ---- Pattern
#  for i in range(len(nums)):
#      while stack and condition(nums[i], nums[stack[-1]]):
#          # Do something with stack[-1]
#          stack.pop()
#      stack.append(i)

def increasing_stack(nums):
    """ Next Greater Element """
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            prev_index = stack.pop()
            res[prev_index] = nums[i]
        stack.append(i)

    return res

def decreasing_stack(nums):
    """ Next smaller element """
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] < nums[stack[-1]]:
            prev_index = stack.pop()
            res[prev_index] = nums[i]
        stack.append(i)
    return res

