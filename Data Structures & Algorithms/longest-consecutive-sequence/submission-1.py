class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0 # track longest consecutive

        for num in num_set:
            if num - 1 not in num_set:
                current = num #get the current value
                count = 1 # track curr consecutive seq

                while current + 1 in num_set:
                    current += 1 # inc loop
                    count += 1
                longest = max(longest, count)
        
        return longest




