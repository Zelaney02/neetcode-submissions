class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # goal is to get the largest value of valid string -> window is valid = len(valid_window) - max_freq_count <= k
        # method: sliding window
        #           - l and r start at 0
        # use hashmap to track count + helper var (optional)

        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k: # need to shrink window until within k
                count[s[l]] -= 1 # dec count to remove l
                l += 1 # shirnk window
            res = max(res, r - l + 1) # take the largest result
        return res




        