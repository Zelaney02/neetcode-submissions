class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # convert to set then compare lengths
        count = 0
        n = 0
        
        count = set(nums)
        c = len(count)
        n = len(nums)

        return (c != n)
        