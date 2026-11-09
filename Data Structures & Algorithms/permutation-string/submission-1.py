from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # my original method tryna optimize is too complicated, we can just check every window of the same length as s1
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        count = Counter(s1)
        window = Counter(s2[:n1])

        if window == count:
            return True
        
        for r in range(n1, n2):
            window[s2[r]] += 1
            # add new char = remove old char

            l = r - n1 # curr_idx - len(window) = start of window
            # check count is 0 before removing entirely
            window[s2[l]] -= 1

            if window[s2[l]] == 0:
                del window[s2[l]]
            
            #check now that len is same
            if window == count:
                return True
        return False

            
            



        