#  https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(nums):
        # first pass: count num zeroes and product without zeroes
        zeroes_count, product = 0, 1
        for num in nums: 
            if num == 0:
                zeroes_count += 1
            else: 
                product *= num
        
        # second pass: verify num of zeroes
        if zeroes_count == 0:
            return [product//num for num in nums]
        elif zeroes_count == 1: 
            return [product if num == 0 else 0 for num in nums ]
        else: 
            return [0 for _ in nums]


def main():
    nums = [1,2,3,4]
    print(Solution.productExceptSelf(nums))
    nums = [-1, 1, 0, -3, 3]
    print(Solution.productExceptSelf(nums))
    

if __name__ == "__main__":
    main()
