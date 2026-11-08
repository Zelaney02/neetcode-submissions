class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Method: sliding window (variable-sized w/ dict)
        # dict already tracks index, no need to remove => more efficient

        n = len(s)
        seen = {}
        longest_count = 0
        l = 0

        for r in range(n):
            # case of consecutive letters
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            
            seen[s[r]] = r
            longest_count = max(r - l + 1, longest_count)
        return longest_count
            
        # Method: sliding-window (variable w/ set), needs to remove duplicates

        # n = len(s)
        # left = 0
        # seen = set()
        # longest = 0

        # for right in range(n):
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left += 1
        #     seen.add(s[right])

        #     longest = max(longest, len(seen))
        # return longest



   









        






            

