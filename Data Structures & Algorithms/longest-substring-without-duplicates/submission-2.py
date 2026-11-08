from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window (variable-sized)
        # need a seen set to check for dupes
        # longest count
        n = len(s)
        seen = defaultdict(int)
        longest_count = 0
        curr_count = 0
        l, r = 0, 0

        while r < n:
            # case of consecutive letters
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
                seen[s[r]] = r
                curr_count = 1
            else:
                seen[s[r]] = r
            longest_count = max(r - l + 1, longest_count)

            r += 1
        return longest_count
            
            
                # "zxyzxyz"


            



















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



   









        






            

