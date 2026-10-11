class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {} # (key, value) -> (number, ind)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in pair:
                return [pair[diff], i]

            pair[nums[i]] = i # always add