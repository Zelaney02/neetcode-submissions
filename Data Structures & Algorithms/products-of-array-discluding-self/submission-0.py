import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 2 pass method
        n = len(nums)
        result = [1] * n

        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i] # gives next val access to prev
        
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right # multiply by curr val from left it
            right *= nums[i]

        return result
