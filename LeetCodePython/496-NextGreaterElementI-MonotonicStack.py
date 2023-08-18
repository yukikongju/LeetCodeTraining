#  https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # solution: monotonic stack - O(m+n)

        # --- 
        results = [-1 for _ in range(len(nums1))]
        stack = []
        index_dict = {num: i for i, num in enumerate(nums1)}

        for i, num in enumerate(nums2):
            while stack and num > stack[-1]:
                val = stack.pop()
                idx = index_dict[val]
                results[idx] = num
            if num in index_dict:
                stack.append(num)
        
        return results
            

