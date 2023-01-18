#  https://leetcode.com/problems/longest-consecutive-sequence/
# Neetcode


#  Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# Sol 1: sort the array and check for longest contiguous subarray => O(nlogn)
# Sol 2: check if element is start of a sequence by looking inside a set; expand 
# => O(n)


def longestConsecutive(nums):
    # 1. create set
    nums_set = set(nums)
    
    # 2. get the longest consecutive elements
    longest = 0
    for num in nums: 
        # check if element start a sequence
        if (num -1) not in nums_set:
            seq_length = 0
            while (num + seq_length) in nums_set: 
                seq_length += 1
            longest = max(longest, seq_length)
    return longest


def test1():
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))
    
def test2():
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive(nums))


def main():
    test1()
    test2()

if __name__ == "__main__":
    main()
