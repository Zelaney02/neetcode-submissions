class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        prev2 = 0
        prev1 = nums[0]
        curr_max = 0

        for i in range(1, n):
            curr_max = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = curr_max
        return curr_max